# Report for Assignment 1


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


Link to commit : [5a98cd267a3d28499469553ef6e4504d2c25f052](https://github.com/NolanO64/matplotlib/commit/5a98cd267a3d28499469553ef6e4504d2c25f052#diff-501b7013d3efa42e08d1cc8dc7a27ee6944fcddb062cd7032249a0031bb01ff4)

<img width="850" alt="image" src="https://github.com/NolanO64/matplotlib/assets/75957824/7d982489-447f-4818-a242-883fab3197b4">




`lib/matplotlib/legend.py/set_bbox_to_anchor`

Link to commit : [0c42901b4508e1f3a0c2d75334fb2d7f2397878d](https://github.com/NolanO64/matplotlib/commit/0c42901b4508e1f3a0c2d75334fb2d7f2397878d#diff-e7a00bb4a353fa623c1d0c1de5c6ca602b7ab38e8906d4842640983133b9196a)

![image](https://github.com/NolanO64/matplotlib/assets/75957824/d3e25188-4150-4f7b-a509-a52b161d30ec)



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

Link to commit : [6698edcfe28dce1e0f42a7c432e56a5a21fdd45a](https://github.com/NolanO64/matplotlib/commit/6698edcfe28dce1e0f42a7c432e56a5a21fdd45a#diff-9c604e3ebce77d5db7e7eb4a4f92a08a8fab56faa8646ecf952ed0a3ad7a233c)


**Old coverage results**

<img width="850" alt="image" src="https://github.com/NolanO64/matplotlib/assets/75957824/ffdcf464-8a63-4f91-b128-87329e29eabb">

**New coverage results**

<img width="854" alt="image" src="https://github.com/NolanO64/matplotlib/assets/75957824/02751737-be92-4624-afc7-1a2e5199b521">


The branch coverage improved from 0% to 100% because new tests were added. These tests now cover all branches, including `ax2_ax1_swap`, `ay2_ay1_swap`, `bx2_bx1_swap`, and `by2_by1_swap`.


**Test for** `lib/matplotlib/legend.py/set_bbox_to_anchor`

Link to commit : [44d973d927a234669b290cd6dafe2b9c69fbfe2d](https://github.com/NolanO64/matplotlib/commit/44d973d927a234669b290cd6dafe2b9c69fbfe2d#diff-1b573023d84935306a147bec7f137e59ae79c3d4f3bbea81152eb0c94b58a579)

**Old coverage results**

![image](https://github.com/NolanO64/matplotlib/assets/75957824/e6575ab0-d75b-46ca-8988-8bc3c4c2ee3c)

**New coverage results**

![image](https://github.com/NolanO64/matplotlib/assets/75957824/c7962b7e-e6ee-4e70-a7bf-8229c5a75fd2)


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
