%global tl_name metapost-colorbrewer
%global tl_revision 48753

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	An implementation of the colorbrewer2.org colours for MetaPost
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/metapost-colorbrewer
License:	gpl3+
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/metapost-colorbrewer.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/metapost-colorbrewer.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides two MetaPost include files that define all the
colorbrewer2.org colours: colorbrewer-cmyk.mp colorbrewer-rgb.mp The
first defines all the colours as CMYK, the second as RGB. Use whichever
one you prefer. For an example of what you can do, and a list of all the
names, have a look at colorbrewer-sampler.mp. You can also see the names
on http://colorbrewer2.org. The package also includes the Python script
used to generate the MP source from the colorbrewer project.

