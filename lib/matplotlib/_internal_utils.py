"""
Internal debugging utilities, that are not expected to be used in the rest of
the codebase.

WARNING: Code in this module may change without prior notice!
"""

from io import StringIO
from pathlib import Path
import subprocess

from matplotlib.transforms import TransformNode


branch_coverage = {
    "graphviz_dump_transform_1": False,
    "graphviz_dump_transform_2": False,
    "graphviz_dump_transform_3": False,
    "graphviz_dump_transform_4": False,
}

def graphviz_dump_transform(transform, dest, *, highlight=None):
    """
    Generate a graphical representation of the transform tree for *transform*
    using the :program:`dot` program (which this function depends on).  The
    output format (png, dot, etc.) is determined from the suffix of *dest*.

    Parameters
    ----------
    transform : `~matplotlib.transform.Transform`
        The represented transform.
    dest : str
        Output filename.  The extension must be one of the formats supported
        by :program:`dot`, e.g. png, svg, dot, ...
        (see https://www.graphviz.org/doc/info/output.html).
    highlight : list of `~matplotlib.transform.Transform` or None
        The transforms in the tree to be drawn in bold.
        If *None*, *transform* is highlighted.
    """

    if highlight is None:
        branch_coverage["graphviz_dump_transform_1"] = True
        highlight = [transform]
    seen = set()

    def recurse(root, buf):
        if id(root) in seen:
            branch_coverage["graphviz_dump_transform_2"] = True
            return
        seen.add(id(root))
        props = {}
        label = type(root).__name__
        if root._invalid:
            branch_coverage["graphviz_dump_transform_3"] = True
            label = f'[{label}]'
        if root in highlight:
            branch_coverage["graphviz_dump_transform_4"] = True
            props['style'] = 'bold'
        props['shape'] = 'box'
        props['label'] = '"%s"' % label
        props = ' '.join(map('{0[0]}={0[1]}'.format, props.items()))
        buf.write(f'{id(root)} [{props}];\n')
        for key, val in vars(root).items():
            if isinstance(val, TransformNode) and id(root) in val._parents:
                buf.write(f'"{id(root)}" -> "{id(val)}" '
                          f'[label="{key}", fontsize=10];\n')
                recurse(val, buf)

    buf = StringIO()
    buf.write('digraph G {\n')
    recurse(transform, buf)
    buf.write('}\n')
    subprocess.run(
        ['dot', '-T', Path(dest).suffix[1:], '-o', dest],
        input=buf.getvalue().encode('utf-8'), check=True)

def print_coverage():
    for branch, hit in branch_coverage.items():
        print(f"{branch} was {'hit' if hit else 'not hit'}")
