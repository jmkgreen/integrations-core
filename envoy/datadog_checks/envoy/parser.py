def reassemble_addresses(seq):
    reassembled = []
    prev = ''

    for s in seq:
        if prev.isdigit():
            try:
                end, port = s.split('_')
            except ValueError:
                end, port = '', ''

            if s.isdigit():
                reassembled[-1] += '.{}'.format(s)
            elif end.isdigit() and port.isdigit():
                reassembled[-1] += '.{}:{}'.format(end, port)
            else:
                reassembled.append(s)
        else:
            reassembled.append(s)

        prev = s

    return reassembled
