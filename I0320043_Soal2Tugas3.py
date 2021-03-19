print("Tugas 3 nomor 2")

aku = {'nama': 'Hafid Maulana', 'hobby': ['Sepak bola' , 'badminton', 'traveling'], 'sosial media': ['(ig)hafid_maull', '(WA)085701784961', '(line)haf1739'],
        'lagu kesukaan': ['yummy', 'loss doll', 'blue jeans'], 'makanan favorit': ['nasi goreng', 'nasi kebuli', 'steak']}
aku['hobby'][1] = 'renang'
aku['sosial media'][0] = '(twitter) Hafid Maulana'
del aku['makanan favorit'][-2:]
aku['hobby'].append('lari-lari')
print(aku)