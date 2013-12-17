import pandas.rpy.common as com
import matplotlib as mpl
import matplotlib.pyplot as plt
import argparse

def main():
    iris = com.load_data('iris')
    feature_means = iris.groupby('Species').mean()

    with mpl.rc_context(fname=args.style):
        feature_means.plot(kind='bar')
        plt.title('Mean Features of Iris Data Set')
        plt.ylabel('Values')
        plt.tight_layout()
        plt.savefig(args.output)


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
