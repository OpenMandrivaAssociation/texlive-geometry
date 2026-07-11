%global tl_name geometry
%global tl_revision 78315

Name:		texlive-%{tl_name}
Epoch:		1
Version:	6.0
Release:	%{tl_revision}.1
Summary:	Flexible and complete interface to document dimensions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/geometry
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/geometry.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/geometry.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/geometry.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(graphics)
Requires:	texlive(iftex)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides an easy and flexible user interface to customize
page layout, implementing auto-centering and auto-balancing mechanisms
so that the users have only to give the least description for the page
layout. For example, if you want to set each margin 2cm without header
space, what you need is just \usepackage[margin=2cm,nohead]{geometry}.
The package knows about all the standard paper sizes, so that the user
need not know what the nominal 'real' dimensions of the paper are, just
its standard name (such as a4, letter, etc.). An important feature is
the package's ability to communicate the paper size it's set up to the
output (whether via DVI \specials or via direct interaction with
pdf(La)TeX).

