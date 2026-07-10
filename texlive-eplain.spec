%global tl_name eplain
%global tl_revision 71409

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.14
Release:	%{tl_revision}.1
Summary:	Extended plain TeX macros
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/eplain
License:	gpl2+
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eplain.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eplain.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eplain.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(babel)
Requires:	texlive(cm)
Requires:	texlive(dehyph)
Requires:	texlive(eplain.bin)
Requires:	texlive(hyph-utf8)
Requires:	texlive(knuth-lib)
Requires:	texlive(latex-fonts)
Requires:	texlive(pdftex)
Requires:	texlive(plain)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
An extended version of the plain TeX format, adding support for
bibliographies, tables of contents, enumerated lists, verbatim input of
files, numbered equations, tables, two-column output, footnotes,
hyperlinks in PDF output and commutative diagrams. Eplain can also load
some of the more useful LaTeX packages, notably graphics, graphicx (an
extended version of graphics), color, autopict (a package instance of
the LaTeX picture code), psfrag, and url.

