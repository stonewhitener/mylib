def timer(proc, *args, **kwargs):
    """
    Measure execution time of the specific function
    """
    import time
    t = time.time()
    proc(*args, **kwargs)
    return time.time() - t
