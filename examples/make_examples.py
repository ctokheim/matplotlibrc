import pandas.rpy.common as com
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from numpy.random import randn
import matplotlib.font_manager as fm
import argparse

def main():
    # simulated brownian motion
    df = pd.DataFrame(randn(1000, 4),
                      index=pd.date_range('1/1/2000', periods=1000),
                      columns=['Legend A', 'Legend B', 'Legend C', 'Legend D'])
    df = df.cumsum()

    # iris data set
    iris = com.load_data('iris')
    feature_means = iris.groupby('Species').mean()

    with mpl.rc_context(rc={'text.usetex': False,
                            'font.family': 'Humor Sans'}, fname=args.style):
        prop = fm.FontProperties(fname='/home/ctokheim/.fonts/Humor-Sans.ttf')
        # line plot of brownian motion
        df.plot()
        plt.title('Brownian Motion')
        plt.ylabel('Simulated Values')
        plt.xlabel('Dates')
        plt.tight_layout()
        plt.savefig(args.output.strip('.png') + '.line.png')
        plt.close()

        # bar plot of iris data set
        plt.xkcd()
        ax = feature_means.plot(kind='bar')
        for label in ax.get_xticklabels() :
            label.set_fontproperties(prop)
        for label in ax.get_yticklabels() :
            label.set_fontproperties(prop)
        handles, labels = ax.get_legend_handles_labels()
        plt.legend(handles, ['Greeny-ness', 'Edible Score', '. . .', 'Profit?'])
        plt.xlabel('Species', fontproperties=prop)
        plt.title('Mean Features of Iris Data Set', fontproperties=prop)
        plt.ylabel('Y Label?', fontproperties=prop)
        plt.tight_layout()
        plt.savefig(args.output.strip('.png') + '.bar.png')
        plt.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generates example figures. '
                                     'Requires matplotlib, pandas, and rpy2.')
    parser.add_argument('-s', '--style',
                        action='store',
                        help='path to matplotlibrc file')
    parser.add_argument('-o', '--output',
                        action='store',
                        help='path to save figure')
    args = parser.parse_args()
    main()
