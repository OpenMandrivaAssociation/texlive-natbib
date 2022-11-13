Name:		texlive-natbib
Version:	20668
Release:	1
Summary:	Flexible bibliography support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/natbib
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/natbib.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/natbib.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/natbib.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides a style with author-year and numbered references, as
well as much detailed of support for other bibliography use.
Provides versions of the standard BibTeX styles that are
compatible with natbib - plainnat, unsrtnat, abbrnat. The
bibliography styles produced by custom-bib are designed from
the start to be compatible with natbib.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/natbib/abbrvnat.bst
%{_texmfdistdir}/bibtex/bst/natbib/plainnat.bst
%{_texmfdistdir}/bibtex/bst/natbib/unsrtnat.bst
%{_texmfdistdir}/tex/latex/natbib/bibentry.sty
%{_texmfdistdir}/tex/latex/natbib/natbib.sty
%doc %{_texmfdistdir}/doc/latex/natbib/README.1st
%doc %{_texmfdistdir}/doc/latex/natbib/README.v831b
%doc %{_texmfdistdir}/doc/latex/natbib/natbib.ltx
%doc %{_texmfdistdir}/doc/latex/natbib/natbib.pdf
%doc %{_texmfdistdir}/doc/latex/natbib/natnotes.pdf
%doc %{_texmfdistdir}/doc/latex/natbib/natnotes.tex
#- source
%doc %{_texmfdistdir}/source/latex/natbib/bibentry.drv
%doc %{_texmfdistdir}/source/latex/natbib/bibentry.dtx
%doc %{_texmfdistdir}/source/latex/natbib/bibentry.ins
%doc %{_texmfdistdir}/source/latex/natbib/natbib.dtx
%doc %{_texmfdistdir}/source/latex/natbib/natbib.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
