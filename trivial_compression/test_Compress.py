from Compress import CompressGene
def test_CompressGene():
    cg = CompressGene()
    cg.compress("acg")
    assert  cg.decompress() == "ACG"