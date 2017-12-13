import argparse
import os
import subprocess

content1 = r'''
\documentclass{ctexart}
 
\usepackage[a4paper,top=3cm,bottom=2cm,left=1.5cm,right=1.5cm,marginparwidth=1.5cm]{geometry}

\usepackage{tabularx}
\usepackage{enumitem}
\usepackage{contour}
\usepackage{lastpage}
\usepackage{fancyhdr}
\usepackage{fancyvrb}
\pagestyle{fancy} 
\fancyhead{}
\fancyfoot{}
\fancyhead[L]{\textit{KEY TERMS OF PERSONAL LOAN AGREEMENT}}
\fancyfoot[R]{Page \thepage\ of \pageref{LastPage}}

\newcolumntype{b}{X}
\newcolumntype{s}{>{\hsize=.5\hsize}X}

\begin{document}

\begin{center}
\textsc{\large Key Terms of Personal Loan Agreement}
\end{center}


\begin{table}[htbp]
    \centering
    \begin{tabularx}{\textwidth}{| s | s | s | s |}
        \hline
        \multicolumn{2}{| l |}{%(school)s}     & %(title)s     & Gamma \\ \hline
        1  & 0         & 2        & 4         \\ \hline
        3  & 1         & 3        & 5         \\ \hline
    \end{tabularx}
\end{table}

\begingroup
    \fontsize{7.5pt}{7.5pt}\selectfont
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
        \item 哈哈
        \item 做麼耶
        \begin{enumerate}[label*=\arabic*.]
            \item 把它拿出來
            \item 揭貸款
        \end{enumerate}
      \end{enumerate}
      \item 還錢
    \end{enumerate}
\endgroup

\begingroup
    \fontsize{8pt}{8pt}\selectfont
    \begin{verbatim}  
        how to set font size here to 10 px ?  
    \end{verbatim}  
\endgroup

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
