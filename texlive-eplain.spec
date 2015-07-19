# revision 33826
# category Package
# catalog-ctan /macros/eplain
# catalog-date 2013-11-21 21:20:37 +0100
# catalog-license gpl2
# catalog-version 3.6
Name:		texlive-eplain
Version:	3.6
Release:	10
Summary:	Extended plain tex macros
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/eplain
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eplain.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eplain.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eplain.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-tetex
Requires:	texlive-pdftex
Requires:	texlive-eplain.bin

%description
A powerfully extended version of the plain format, adding
support for bibliographies, tables of contents, enumerated
lists, verbatim input of files, numbered equations, tables,
two-column output, footnotes, hyperlinks in PDF output and
commutative diagrams. Eplain can also load some of the more
useful LaTeX packages, notably graphics, graphicx, color,
autopict (a package instance of the LaTeX picture code),
psfrag, and url.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/eplain/arrow.tex
%{_texmfdistdir}/tex/eplain/btxmac.tex
%{_texmfdistdir}/tex/eplain/eplain.aux
%{_texmfdistdir}/tex/eplain/eplain.ini
%{_texmfdistdir}/tex/eplain/eplain.tex
%_texmf_fmtutil_d/eplain
%doc %{_texmfdistdir}/doc/eplain/AUTHORS
%doc %{_texmfdistdir}/doc/eplain/COPYING
%doc %{_texmfdistdir}/doc/eplain/ChangeLog
%doc %{_texmfdistdir}/doc/eplain/INSTALL
%doc %{_texmfdistdir}/doc/eplain/NEWS
%doc %{_texmfdistdir}/doc/eplain/README
%doc %{_texmfdistdir}/doc/eplain/demo/Makefile
%doc %{_texmfdistdir}/doc/eplain/demo/lscommnt.tex
%doc %{_texmfdistdir}/doc/eplain/demo/xhyper.tex
%doc %{_texmfdistdir}/doc/eplain/eplain.html
%doc %{_texmfdistdir}/doc/eplain/eplain.pdf
%doc %{_texmfdistdir}/doc/eplain/lscommnt.jpg
%doc %{_texmfdistdir}/doc/eplain/util/idxuniq
%doc %{_texmfdistdir}/doc/eplain/util/trimsee
%doc %{_texmfdistdir}/doc/eplain/xhyper.jpg
%doc %{_infodir}/eplain.info*
%doc %{_mandir}/man1/eplain.1*
%doc %{_texmfdistdir}/doc/man/man1/eplain.man1.pdf
#- source
%doc %{_texmfdistdir}/source/eplain/eplain-source-3.6.zip
%doc %{_texmfdistdir}/source/eplain/xeplain.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_infodir}
mv %{buildroot}%{_texmfdistdir}/doc/info/*.info %{buildroot}%{_infodir}
mkdir -p %{buildroot}%{_texmf_fmtutil_d}
cat > %{buildroot}%{_texmf_fmtutil_d}/eplain <<EOF
#
# from eplain:
eplain pdftex language.dat -translate-file=cp227.tcx *eplain.ini
EOF
