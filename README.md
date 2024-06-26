﻿# Report for Assignment 1


## Project chosen


Name: matplotlib


URL: https://github.com/matplotlib/matplotlib


Number of lines of code and the tool used to count it: Lizard - 229 KOC


Programming language: Python


## Coverage measurement


### Existing tool


The tool we use to perform coverage analysis is `Coverage.py`.


**Execution:**


```sh
coverage run -m pytest
coverage report
```


**Screenshot of Coverage Results:**


<img width="655" alt="image" src="https://github.com/NolanO64/matplotlib/assets/75957824/9a1e39c5-4be8-4dc4-8461-19236c096539">



### Your own coverage tool



**Nolan Otam**


`lib/matplotlib/transforms.py/overlaps`


Link to commit : [945fe2a4151d5aa2ddb360d51b386002219f2231](https://github.com/NolanO64/matplotlib/commit/945fe2a4151d5aa2ddb360d51b386002219f2231)

<img width="1246" alt="image" src="https://github.com/NolanO64/matplotlib/assets/75957824/a6dd6d43-a484-40e6-bd3b-9970b5e39e2a">




`lib/matplotlib/legend.py/set_bbox_to_anchor`

Link to commit : [0c42901b4508e1f3a0c2d75334fb2d7f2397878d](https://github.com/NolanO64/matplotlib/commit/0c42901b4508e1f3a0c2d75334fb2d7f2397878d)

<img width="1243" alt="image" src="https://github.com/NolanO64/matplotlib/assets/75957824/7c3d4fa2-1345-4ed1-8473-1f21acd88976">



**Moegiez Bhatti**


`first function`


<Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements>


<Provide a screenshot of the coverage results output by the instrumentation>


`second function`


<Provide the same kind of information provided for Function 1>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements>


<Provide a screenshot of the coverage results output by the instrumentation>

**Narek Darbinyan**


`first function`


<Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements>


<Provide a screenshot of the coverage results output by the instrumentation>


`second function`


<Provide the same kind of information provided for Function 1>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements>


<Provide a screenshot of the coverage results output by the instrumentation>

**Eric Pătrașcu**


`first function`


<Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements>


<Provide a screenshot of the coverage results output by the instrumentation>


`second function`


<Provide the same kind of information provided for Function 1>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements>


<Provide a screenshot of the coverage results output by the instrumentation>



## Coverage improvement


### Individual tests


<The following is supposed to be repeated for each group member>


**Nolan Otam**

**Test for** `lib/matplotlib/transforms.py/overlaps`

Link to commit : [44d973d927a234669b290cd6dafe2b9c69fbfe2d](https://github.com/NolanO64/matplotlib/commit/44d973d927a234669b290cd6dafe2b9c69fbfe2d)


**Old coverage results**

<img width="1246" alt="image" src="https://github.com/NolanO64/matplotlib/assets/75957824/a6dd6d43-a484-40e6-bd3b-9970b5e39e2a">

**New coverage results**

<img width="1244" alt="image" src="https://github.com/NolanO64/matplotlib/assets/75957824/345f3a89-5041-4deb-9d52-0f6d6ecddc54">


The branch coverage improved from 0% to 100% because new tests were added. These tests now cover all branches, including `ax2_ax1_swap`, `ay2_ay1_swap`, `bx2_bx1_swap`, and `by2_by1_swap`.


**Test for** `lib/matplotlib/legend.py/set_bbox_to_anchor`

Link to commit : [44d973d927a234669b290cd6dafe2b9c69fbfe2d](https://github.com/NolanO64/matplotlib/commit/44d973d927a234669b290cd6dafe2b9c69fbfe2d)

**Old coverage results**

<img width="1243" alt="image" src="https://github.com/NolanO64/matplotlib/assets/75957824/7c3d4fa2-1345-4ed1-8473-1f21acd88976">

**New coverage results**

<img width="1250" alt="image" src="https://github.com/NolanO64/matplotlib/assets/75957824/30d64ddd-d11e-46ed-8e0e-511e69539f59">


The branch coverage improved from 57% to 100% because new tests were added. These tests now cover previously untested branches, including cases for `bbox_is_BboxBase_instance`, `bbox_length_is_not_2`, and `transform_is_not_None`.
  

### Overall

**Old global coverage results**

<img width="655" alt="image" src="https://github.com/NolanO64/matplotlib/assets/75957824/9a1e39c5-4be8-4dc4-8461-19236c096539">

**New global coverage results**

<Provide a screenshot of the new coverage results by running the existing tool using all test modifications made by the group>


## Statement of individual contributions


<Write what each group member did>


**Nolan Otam**

- Branch coverage analysis of `lib/matplotlib/transforms.py/overlaps`
- Added tests to improve branch coverage of `lib/matplotlib/transforms.py/overlaps`
- Branch coverage analysis of `lib/matplotlib/legend.py/set_bbox_to_anchor`
- Added tests to improve branch coverage of `lib/matplotlib/legend.py/set_bbox_to_anchor`
