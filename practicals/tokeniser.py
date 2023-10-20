import sys

s = sys.stdin.readline()
index = 1

while s:
    print('# sent_id = %d' % (index))
    index += 1
    print('# text = %s' % (s.strip()))

    tokens = s.strip().split(" ")  
    token_index = 0
    for ss in tokens:
        token_index += 1
        print(token_index, ss, end='\t')
        

        for _ in range(10):
            print('_', end='\t')
        print()

    s = sys.stdin.readline()


