Name:		texlive-eplain
Version:	71409
Release:	1
Summary:	Extended plain tex macros
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/eplain
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eplain.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eplain.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eplain.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/eplain
%_texmf_fmtutil_d/eplain
%doc %{_texmfdistdir}/doc/eplain
%doc %{_infodir}/eplain.info*
%doc %{_mandir}/man1/eplain.1*
%doc %{_texmfdistdir}/doc/man/man1/eplain.man1.pdf
#- source
%doc %{_texmfdistdir}/source/eplain

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

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
