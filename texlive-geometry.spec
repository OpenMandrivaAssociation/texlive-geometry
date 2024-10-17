Name:		texlive-geometry
Version:	61719
Release:	2
Summary:	Flexible and complete interface to document dimensions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/geometry
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/geometry.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/geometry.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/geometry.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides an easy and flexible user interface to
customize page layout, implementing auto-centering and auto-
balancing mechanisms so that the users have only to give the
least description for the page layout. For example, if you want
to set each margin 2cm without header space, what you need is
just \usepackage[margin=2cm,nohead]{geometry}. The package
knows about all the standard paper sizes, so that the user need
not know what the nominal 'real' dimensions of the paper are,
just its standard name (such as a4, letter, etc.). An important
feature is the package's ability to communicate the paper size
it's set up to the output (whether via DVI \specials or via
direct interaction with PDF(La)TeX).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/geometry
%doc %{_texmfdistdir}/doc/latex/geometry
#- source
%doc %{_texmfdistdir}/source/latex/geometry

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
