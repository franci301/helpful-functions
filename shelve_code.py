import shelve

def load():
    s = shelve.open('test')
    try:
        data = s['dealers']
    except KeyError:
        data = {}
        s['dealers'] = data
    finally:
        s.close()
    return data



def write(d):
    s = shelve.open('test')
    data = load()
    for i in d:
        dealer = i.split(' ')[0]
        product = i.split(' ')[1]
        if dealer not in data:
            data[dealer] = [product]
        elif product not in data[dealer]:
            data[dealer].append(product)
    s['dealers'] = data
    s.close()

            
dealer_prod = ['A B','B C', 'C D']
write(dealer_prod)
data = load()
print(data)