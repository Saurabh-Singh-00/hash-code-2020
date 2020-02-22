# Google Hash Code 2020
Our submission for Google Hash Code 2020. Even though we could not complete our submission during the Hash Code hours, we continued the hunt for our solution. The submission that we made are for the **Extended Round**.

### Team Members

------------

- [Rohit Sahoo](https://github.com/sahoo-rohit "Rohit Sahoo")
- [Rushikesh Chaudhari](https://github.com/Reyano132 "Rushikesh Chaudhari")
- [Vedang Naik](https://github.com/vedang08 "Vedang Naik")
- [Saurabh Singh](https://github.com/Saurabh-Singh-00 "Saurabh Singh")

### Approach

------------

- To maximize the scanning score we calculated the throughput for each library using the below formula.

- ![Equation](https://raw.githubusercontent.com/Saurabh-Singh-00/hash-code-2020/master/images/equation.png "Equation")

- The Libraries are then sorted in *O(logN)* based on their throughput so that the library with maximum throughput can be selected first.

- If the Signup period of the selected library is less than the TOTAL_DAYS remaining then the libraries can be signed up and dispatched for scanning.

- Maximum score can be attained if all the books are scanned within the time frame atleast once as illustrated below.

- ![Maximum Scans](https://raw.githubusercontent.com/Saurabh-Singh-00/hash-code-2020/master/images/library.PNG "Maximum Scans")

### Result

------------

- The results that we achieved was quite satisfactory

![Results](https://raw.githubusercontent.com/Saurabh-Singh-00/hash-code-2020/master/images/total_score.PNG "Results")
