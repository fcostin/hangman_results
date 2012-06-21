import string

import result_database as result_database

COLOUR = {
    'win_minimax' : '#0A9269;',
    'win_thought' : '#25604E;',
    'loss_minimax' : '#DD5710;',
    'loss_thought' : '#915739;',
    'loss_exclude_bound' : '#732A03;',
}

def render_table(results):
    max_word_length = 31
    max_lives = 26
    word_lengths = range(1, max_word_length + 1)
    lives = range(0, max_lives + 1)

    import numpy
    table = numpy.zeros((max_word_length + 1, max_lives + 1), dtype='S1')
    table[:, :] = '?'
    style = {}

    # there are no words of length 26 or 30
    table[26, :] = '-'
    table[30, :] = '-'

    for result in results:
        i = result.word_length
        j = result.lives
        if result.outcome == "win":
            for j_prime in range(j, max_lives + 1):
                if (i, j_prime) not in style:
                    table[i, j_prime] = 'W'
                    style[(i, j_prime)] = 'win_' + result.method.lower()
                    assert style[(i, j_prime)] in COLOUR
        elif result.outcome == "loss":
            for j_prime in range(0, j + 1):
                if (i, j_prime) not in style:
                    table[i, j_prime] = 'L'
                    style[(i, j_prime)] = 'loss_' + result.method.lower()
                    assert style[(i, j_prime)] in COLOUR

    output = []
    def p(line, newline=True):
        if newline:
            line = line + '\n'
        output.append(line)
   
    p('<table>')
    p('<thead>')
    p('\t<tr>', newline=False)
    p('<td>Lives</td>', newline=False)
    p('<td colspan=%d>Word Length</td>' % len(word_lengths), newline=False)
    p('</tr>')
    p('\t<tr>', newline=False)
    p('<td></td>', newline=False)
    for i in word_lengths:
        p('<td>%d</td>' % i, newline=False)
    p('</tr>')
    p('</thead>')
    p('<tbody>')
    for j in lives:
        p('\t<tr>', newline=False)
        p('<td>%d</td>' % j, newline=False)
        for i in word_lengths:
            css_class = style.get((i, j), '')
            p('<td class="%s">%s</td>' % (css_class, chr(table[i, j][0])), newline=False)
        p('</tr>')
    p('</tbody>')
    p('</table>')

    return ''.join(output)

table = render_table(result_database.DATA)
with open('index.html.template', 'r') as f:
    index_template = string.Template(f.read())
with open('index.html', 'w') as f_out:
    text = index_template.substitute(TABLE_OF_RESULTS = table)
    f_out.write(text)
