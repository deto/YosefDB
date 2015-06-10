def handle_uploaded_file(f):
    import pdb; pdb.set_trace();
    with open('test.txt', 'wb+') as fout:
        for chunk in f.chunks():
            fout.write(chunk);