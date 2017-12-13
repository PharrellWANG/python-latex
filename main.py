import argparse
import os
import subprocess

content1 = r'''
\documentclass{ctexart}
 
\usepackage[a4paper,top=3cm,bottom=2cm,left=1.5cm,right=1.5cm,marginparwidth=1.5cm]{geometry}

\usepackage{tabularx}
\usepackage{enumitem}

\usepackage{lastpage}
\usepackage{lastpage}
\usepackage{fancyhdr}
\pagestyle{fancy} 

\cfoot{\thepage\ of \pageref{LastPage}}
\newcolumntype{b}{X}
\newcolumntype{s}{>{\hsize=.5\hsize}X}

\begin{document}

\begin{center}
    \LARGE\bf
    M\textsc{emorandum}
\end{center}


\begin{table}[htbp]
    \centering
    \begin{tabularx}{\textwidth}{| s | s | s | s |}
        \hline
        \multicolumn{2}{| l |}{Alpha}     & Beta     & Gamma     \\ \hline
        1  & 0         & 2        & 4         \\ \hline
        3  & 1         & 3        & 5         \\ \hline
    \end{tabularx}
\end{table}

\begin{enumerate}[label*=\arabic*.]
  \item \textbf{\underline{First}}
  \begin{enumerate}[label*=\arabic*.]
    \item Second
    \item Third
    \begin{enumerate}[label*=\arabic*.]
        \item Second
        \item Third
    \end{enumerate}
  \end{enumerate}
  \item Fourth
\end{enumerate}

\begin{enumerate}[label*=\arabic*.]
  \item \textbf{\underline{鍾文}}
  \begin{enumerate}[label*=\arabic*.]
    \item Second
    \item Third
    \begin{enumerate}[label*=\arabic*.]
        \item Second
        \item Third
    \end{enumerate}
  \end{enumerate}
  \item Fourth
\end{enumerate}


\end{document}'''

parser = argparse.ArgumentParser()
# parser.add_argument('-c', '--course', default='Course')
parser.add_argument('-t', '--title', default='Title')
# parser.add_argument('-n', '--name', default='Name')
parser.add_argument('-s', '--school', default='My U')

args = parser.parse_args()

with open('cover.tex', 'w') as f:
    f.write(content1 % args.__dict__)

cmd = ['xelatex', '-interaction', 'nonstopmode', 'cover.tex']
# cmd = ['pdflatex', '-interaction', 'nonstopmode', 'cover.tex']
sub_pro = subprocess.Popen(cmd)
sub_pro.communicate()

ret_code = sub_pro.returncode
if not ret_code == 0:
    os.unlink('cover.pdf')
    raise ValueError(
        'Error {} executing command: {}'.format(ret_code, ' '.join(cmd)))

cmd = ['xelatex', '-interaction', 'nonstopmode', 'cover.tex']
# cmd = ['pdflatex', '-interaction', 'nonstopmode', 'cover.tex']
sub_pro = subprocess.Popen(cmd)
sub_pro.communicate()

ret_code = sub_pro.returncode
if not ret_code == 0:
    os.unlink('cover.pdf')
    raise ValueError(
        'Error {} executing command: {}'.format(ret_code, ' '.join(cmd)))

os.unlink('cover.tex')
os.unlink('cover.log')
os.unlink('cover.aux')
