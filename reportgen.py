import matplotlib.pyplot as plt

def create_fig():
    # NOTE: matplotlib retains a global reference to the current figure
    # this means we don't need to pass the resulting object around
    plt.figure()
    fig = plt.gcf()
    fig.set_size_inches(8.5, 11)
    plt.clf()


def create_title_page(pdf, text, subtitle=''):
    create_fig()
    plt.text(0.5, 0.9, text, horizontalalignment='center', fontsize=14)
    plt.text(0.5, 0.6, subtitle, horizontalalignment='center', fontsize=10)
    plt.axis('off')

    pdf.savefig(plt.gcf())
    plt.close()


def create_text_page(pdf, text):
    create_fig()

    plt.axis('off')
    y = 1.0
    for line in text:
        plt.text(0.0, y, line, fontsize=8)
        y -= 0.03
        if y < 0.05:
            pdf.savefig(plt.gcf())
            plt.clf()
            plt.axis('off')
            y = 1.0
    pdf.savefig(plt.gcf())
    plt.close()


def create_table_page(pdf, col1, col2, col3, col4, decoration):
    create_fig()

    plt.axis('off')
    y = 1.0
    for i in range(0, len(col1)):
        if decoration[i] is None:
            weight = 'normal'
            color  = 'black'
        elif decoration[i] == 'red':
            weight = 'normal'
            color  = 'red'
        elif decoration[i] == 'bold':
            weight = 'bold'
            color  = 'black'

        plt.text(0.0, y, col1[i], fontsize=8, fontweight=weight, color=color)
        plt.text(0.4, y, col2[i], fontsize=8, fontweight=weight, color=color)
        plt.text(0.7, y, col3[i], fontsize=8, fontweight=weight, color=color)
        plt.text(0.9, y, col4[i], fontsize=8, fontweight=weight, color=color)

        y -= 0.02
        if y < 0.02:
            pdf.savefig(plt.gcf())
            plt.clf()
            plt.axis('off')
            y = 1.0
    pdf.savefig(plt.gcf())
    plt.close()
