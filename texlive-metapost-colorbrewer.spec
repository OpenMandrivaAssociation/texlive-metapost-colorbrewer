Name:		texlive-metapost-colorbrewer
Version:	48753
Release:	2
Summary:	An implementation of the colorbrewer2.org colours for MetaPost
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/metapost-colorbrewer
License:	gpl3+
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metapost-colorbrewer.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metapost-colorbrewer.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides two MetaPost include files that define
all the colorbrewer2.org colours: colorbrewer-cmyk.mp
colorbrewer-rgb.mp The first defines all the colours as CMYK,
the second as RGB. Use whichever one you prefer. For an example
of what you can do, and a list of all the names, have a look at
colorbrewer-sampler.mp. You can also see the names on
http://colorbrewer2.org. The package also includes the Python
script used to generate the MP source from the colorbrewer
project.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/metapost/metapost-colorbrewer
%doc %{_texmfdistdir}/doc/metapost/metapost-colorbrewer

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
