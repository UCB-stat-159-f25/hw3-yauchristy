import numpy as np
import pytest
from ligotools.readligo import loaddata, getstrain, getsegs

def test_loaddata():
    file_path = 'data/H-H1_LOSC_4_V2-1126259446-32.hdf5'
    strain, time, channel_dict = loaddata(file_path, 'H1')
    assert isinstance(channel_dict, dict)

def test_getstrain():
    segList = getsegs(842657792, 842658792, 'H1')
    for (start, stop) in segList:
        strain, meta, dq = getstrain(start, stop, 'H1')
        assert isinstance(meta, dict)
        