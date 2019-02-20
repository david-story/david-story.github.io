---
layout: pages
title:  "Python Practice Examples"
minimal_mistakes_skin    : "dark"
---

Below are few Python files that work through examples of a variety of different operations, functions
syntax, and some library functionalities. You may find these useful when working on your workshop or 
just learning about a few new libraries or tips and tricks.

## Example Python Files: ##
<ul style="list-style-type:disc">
<li><a href="/assets/code/practice-example-one.py">Practice Example 1</a> - Basics of Python including variables, datatypes, arithmetic, and functions.</li>
<li><a href="/assets/code/practice-example-two.py">Practice Example 2</a> - Basics on conditional logic, loops, and lists</li>
<li><a href="/assets/code/practice-example-three.py">Practice Example 3</a> - Basics on number representation (decimal & hex), ASCII, and bit operators</li>
<li><a href="/assets/code/practice-example-four.py">Practice Example 4</a> - Basic functions on some included Python Libraries</li>
</ul>

Below are links to Python tutor examples. These are examples that you can step through with a browser based Python interpreter.
This is nice to visualize and helps you see how each step is executed, allowing you to help understand some of the logic or find
an error in your code.

## Python Tutor Examples ##

<ul style="list-style-type:disc">
<li><a href="http://pythontutor.com/visualize.html#code=%23%20Example%20of%20bit%20masking%0A%0A%23%20Byte%3A%201111%201111%0Abyte%20%3D%200xFF%0A%0A%23%20We%20just%20want%20the%20LSB%20%28least%20significat%20bit%29%0A%0A%23%20mask%3A%200000%200001%0Amask%20%3D%200x01%0A%0A%23%201111%201111%20AND%200000%200001%0A%23%20-----------------------%0A%23%20result%3A%200000%200001%0A%0Aresult%20%3D%20byte%20%26%20mask%0A%0Aprint%28hex%28result%29%29%0A%0A%23%20Say%20we%20want%20to%20do%20this%20as%20a%20boolean%20test%0Aif%28result%29%3A%0A%20%20%20%20print%28%22The%20LSB%20is%20set%22%29%0Aelse%3A%0A%20%20%20%20print%28%22The%20LSB%20is%20not%20set%22%29%0A%20%20%20%20%0A%23%20Try%20inputting%20your%20own%20byte%20and%20testing%20if%20the%20LSB%20is%20set%0Atry%3A%0A%20%20%20%20%23%20you%20input%20some%20integer%0A%20%20%20%20your_input%20%3D%20int%28input%28%22Input%20some%20number%3A%22%29%29%0A%20%20%20%20%23%20your%20input%20is%20and's%20with%20the%20bit%20mask%0A%20%20%20%20new_result%20%3D%20your_input%20%26%20mask%0A%20%20%20%20%23%20prints%20results%0A%20%20%20%20if%28new_result%29%3A%0A%20%20%20%20%20%20%20%20print%28%22The%20LSB%20is%20set%22%29%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20print%28%22The%20LSB%20is%20not%20set%22%29%0A%20%20%20%20%0Aexcept%3A%0A%20%20%20%20%23%20input%20to%20your_input%20not%20a%20number,%20error%0A%20%20%20%20print%28%22Make%20sure%20to%20input%20a%20number!%22%29&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%220%22%5D&textReferences=false
">Python Tutor Example 1</a> - Basics of bit masking.</li>
<li><a href="http://pythontutor.com/visualize.html#code=a%20%3D%20True%0Ab%20%3D%20True%0A%0A%23%20If%20a%20is%20true%0Aif%20a%20%3D%3D%20False%3A%0A%20%20%20%20%23%20we%20will%20only%20print%20this%0A%20%20%20%20print%28%22a%20is%20false%22%29%0A%23%20but%20is%20a%20is%20not%20true%20and%20b%20is%20false,%0Aelif%20b%20%3D%3D%20False%3A%0A%20%20%20%20%23%20we%20will%20print%20this%0A%20%20%20%20print%28%22b%20is%20false%22%29%0A%23%20if%20all%20the%20if%20or%20elif%20statements%20above%20fail%0Aelse%3A%0A%20%20%20%20%23%20we%20catch%20all!%0A%20%20%20%20print%28%22neither%20are%20false%22%29%0A%20%20%20%20%0Aif%20a%20%3D%3D%20True%3A%0A%20%20%20%20print%28%22a%20is%20true%22%29%0Aif%20b%20%3D%3D%20True%3A%0A%20%20%20%20print%28%22b%20is%20true%22%29%0A%20%20%20%20%0A&cumulative=false&curInstr=9&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false">
Python Tutor Example 2</a> - Examples of conditionals</li>
</ul>

<li><a href="http://pythontutor.com/visualize.html#code=sample_numbers%20%3D%20%5B1234,5345,4564,3457,2435,2345245%5D%0A%0Afor%20numbers%20in%20sample_numbers%3A%0A%20%20%20%20print%28%22Sample%3A%20%22,%20numbers,%20end%3D%22%20%22%29%0A%20%20%20%20print%28%22Sample%20in%20HEX%3A%22,%20hex%28numbers%29,%20end%3D%22%20%22%29%0A%20%20%20%20print%28%22Sample%20in%20Binary%3A%22,%20bin%28numbers%29%29&cumulative=false&curInstr=26&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false">
Python Tutor Example 3</a> - Integers to hex to binary</li>


