#!/usr/bin/env python
from Bio import SeqIO
from Bio import AlignIO
from Bio import Phylo
from Bio.Phylo import draw
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor,DistanceCalculator
from ntpath import basename
import subprocess
import argparse
import os
import matplotlib.pyplot as plt 
import matplotlib



#get arguments
parser = argparse.ArgumentParser(description='Quick and easy tree reconstruction')
parser.add_argument('--input',help='Input fasta file',type=str,required=True)
parser.add_argument('--output',help='Output directory',type=str,required=True)
parser.add_argument('-phylipf',help='Phylip format relaxed or sequential. Default is sequential',type=str,default='sequential')
parser.add_argument('-model',help='Choose model, identity for dna or blosum62 for protein. Default is blosum62',type=str,default='identity')
parser.add_argument('-method',help='Choose tree reconstruction method nj or upgma.Default is nj.',type=str,default='nj')
args = parser.parse_args()



def convert_to_phylip(alnfile,phyformat):
    '''
    Convert fasta alignment to phylip format
    Returns filename
    '''
    aln = AlignIO.read(alnfile,'fasta')
    phyfile = alnfile[:alnfile.find('.')]+'.phy'
    AlignIO.write(aln,phyfile,'phylip-'+phyformat)

    return phyfile



def tree_reconstruction(phy_file,method,model,phyformat):
    '''Construct tree with given method and model'''

    aln = AlignIO.read(phy_file,'phylip-'+phyformat)
    
    constructor = DistanceTreeConstructor()
    calculator = DistanceCalculator(model)
    dm = calculator.get_distance(aln)

    if method == 'upgma':
        tree = constructor.upgma(dm)
    elif method == 'nj':
        tree = constructor.nj(dm)

    tree.ladderize()

    for c in tree.find_clades():
        if 'Inner' in c.name:
            c.name = ''

    Phylo.write(tree,args.output+'/tree.nwk','newick')

    plt.rcParams['font.style'] = 'italic'
    plt.rc('font',size=8)
    plt.rc('axes',titlesize=14)
    plt.rc('xtick',labelsize=10)
    plt.rc('ytick',labelsize=10)
    plt.rc('figure',titlesize=18)

    draw(tree,do_show=False)
    plt.savefig(args.output+"/tree.svg",format='svg',dpi=1200)
    
def main():
    
    #results directory
    if not os.path.isdir(args.output):
        os.mkdir(args.output)

    #align sequences with muscle
    print("\nPerforming alignment with muscle.\n")
    
    base = basename(args.input)
    aln_outfile = args.output+'/'+'aln_'+base
    subprocess.run(['muscle','-in',args.input,'-out',aln_outfile])
    
    #refine alignment
    print('\nRefining alignment with muscle.\n')

    aln_outfile_refined  = args.output+'/'+'aln_refined_'+base
    subprocess.run(['muscle','-in',aln_outfile,'-out',aln_outfile_refined])



    #convert to phylip format
    print('\nConverting fasta alignment to phylip format.\n')
    try:
        refined_file_for_tree = convert_to_phylip(aln_outfile_refined,args.phylipf)
    except ValueError as ex:

        error_msg = ex.args[0]
        if 'repeated' in error_msg.lower():
            print(error_msg,'\n')
            print('Try relaxed phylip format.')
        else:
            print(error_msg)
    else:
        #reconstruct tree with distance method
        print('Contructing tree')
        tree_reconstruction(refined_file_for_tree,args.method,args.model,args.phylipf)


if __name__ == '__main__':
    main()
