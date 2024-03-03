def test_median_finder(MedianFinder, benchmark):
    finder = MedianFinder()
    finder.addNum(1)
    assert finder.peek() == (1, None)
    assert finder.findMedian() == 1
    finder.addNum(2)
    assert finder.peek() == (1, 2)
    assert finder.findMedian() == 1.5
    finder.addNum(5)
    assert finder.peek() == (1, 2)
    assert finder.findMedian() == 2
    finder.addNum(4)
    assert finder.peek() == (2, 4)
    assert finder.findMedian() == 3
    finder.addNum(1000)
    assert finder.peek() == (2, 4)
    assert finder.findMedian() == 4
    benchmark(finder.addNum, 20)


def test_median_finder_2(MedianFinder, benchmark):
    finder = MedianFinder()
    finder.addNum(5)
    finder.addNum(2)
    finder.addNum(1)
    assert finder.peek() == (2, 5)
    assert finder.findMedian() == 2
    finder.addNum(0)
    assert finder.peek() == (1, 2)
    assert benchmark(finder.findMedian) == 1.5


def test_median_finder_edge(MedianFinder):
    finder = MedianFinder()
    finder.addNum(0)
    assert finder.peek() == (0, None)
    assert finder.findMedian() == 0
    finder.addNum(0)
    assert finder.peek() == (0, 0)
    assert finder.findMedian() == 0


def test_median_finder_edge_2(MedianFinder):
    finder = MedianFinder()
    assert finder.findMedian() is None
