import pickle


def pickle_data():
    data = {
        'name': 'Prashant',
        'profession': 'Software Engineer',
        'country': 'India'
    }
    filename = 'PersonalInfo'
    outfile = open(filename, 'wb')
    pickle.dump(data, outfile)
    outfile.close()


pickle_data()