import pytest 
import sys 
import os 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import facenet
from facenet.utils import download 

'''
download module's function are added mostly for download already trained modules that are uploaded and released on the remote server. 

in unit test case we test its download function by 
downloading the training datasets from lfw(http://vis-www.cs.umass.edu/lfw/#views)
whichi is short for the 'Labeled Faces in the Wild'. 
'''


'''
case1:
in unit test case1 we test download remote facial dataset by 
url: given valid remote download url address
dst: valid local file path 
hash_prefix: disable sha256 by passing None 
progress: True show the download progress visual 
'''
def test_download_url_to_file_case1(): 
    print("test: download_url_to_file")
    url = "http://vis-www.cs.umass.edu/lfw/pairsDevTrain.txt"
    dst = "/tmp/lfw_pairsDevTrain.txt"
    hash_prefix=None
    progress = True
    download.download_url_to_file(url=url, dst=dst, hash_prefix=hash_prefix, progress=progress)

'''
case2:
in unit test case1 we test download remote facial dataset by 
url: given valid remote download url address
dst: valid local file path 
hash_prefix: disabled
progress: False show the download progress visual 
'''
def test_download_url_to_file_case2():
    print("case2: download_url_to_file")
    url = "http://vis-www.cs.umass.edu/lfw/pairsDevTest.txt"
    dst = "/tmp/lfw_pairsDevTest.txt"
    hash_prefix = None
    progress = False 
    download.download_url_to_file(url=url, dst=dst, hash_prefix=hash_prefix, progress=progress)


'''
case3:
in unit test case1 we test download remote facial dataset by 
url: given an in-valid remote download url address
dst: valid local file path 
hash_prefix: disabled
progress: False show the download progress visual 
'''
@pytest.mark.xfail
def test_download_url_to_file_case3():
    print("case3: download_url_to_file")
    # invalid url given should be failed which already decorated by the annotation(pytest.mark.xfail)
    url = "http://vis-www.cs.umass.edu/lfw/peopleDevxrain.txt"
    dst = "/tmp/lfw_peopleDevTrain.txt"
    hash_prefix = None
    progress = True 
    download.download_url_to_file(url=url, dst=dst, hash_prefix=hash_prefix, progress=progress)