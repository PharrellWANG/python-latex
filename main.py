import argparse
import os
import subprocess

content1 = r'''
\documentclass{ctexart}
 
\usepackage[a4paper,top=3cm,bottom=2cm,left=1.5cm,right=1.5cm,marginparwidth=1.5cm]{geometry}

\usepackage{tabularx}
\usepackage{lastpage}
\usepackage{enumitem}

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

content2 = r'''
\documentclass{article}
\usepackage[a4paper,top=3cm,bottom=2cm,left=3cm,right=3cm,marginparwidth=1.75cm]{geometry}
\usepackage{tabularx}

\newcolumntype{b}{X}
\newcolumntype{s}{>{\hsize=.5\hsize}X}
\newcommand{\heading}[1]{\multicolumn{1}{c}{#1}}

\begin{document}

\begin{table}[htbp]
    \centering
    \begin{tabularx}{\textwidth}{|b|s|s|}
        \hline
        \heading{Alpha}     & \heading{Beta}     & \heading{Gamma}     \\ \hline
        0         & 2        & 4         \\ \hline
        1         & 3        & 5         \\ \hline
    \end{tabularx}
\end{table}
\end{document}
'''

content3 = r'''
\documentclass{article}
\usepackage[a4paper,top=3cm,bottom=2cm,left=3cm,right=3cm,marginparwidth=1.75cm]{geometry}
\begin{document}

\begin{table}[htbp]
    \caption{Time saving for wedgelet searching and coding performance of proposed method}
    \bigskip\label{tab:ts-dmm}
    \centering
    \begin{tabular}{c c c c c c c}
        \toprule
        & \multicolumn{4}{c}{Time saving for DMM1} & & \\\cline{2-5}
        Sequences & QP34 & QP39 & QP42 & QP45 & BD-BR & BD-PSNR \\
        \midrule
        Newspaper       & 63.76 & 64.94 & 71.98 & 74.14 & 0.98\% & -0.02dB \\
        PoznanHall2    & 71.08 & 71.08 & 66.36 & 71.27 & 1.64\% & -0.05dB \\
        GhostTownFly       & 62.00 & 56.20 & 51.60 & 58.87 & 0.65\% & -0.02dB \\
        Shark           & 63.55 & 58.66 & 63.26 & 63.34 & 1.04\% & -0.03dB \\
    \end{tabular}
\end{table}

\end{document}
'''

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

os.unlink('cover.tex')
os.unlink('cover.log')
os.unlink('cover.aux')
