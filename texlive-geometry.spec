# revision 19716
# category Package
# catalog-ctan /macros/latex/contrib/geometry
# catalog-date 2010-09-13 00:36:13 +0200
# catalog-license lppl
# catalog-version 5.6
Name:		texlive-geometry
Version:	5.6
Release:	8
Summary:	Flexible and complete interface to document dimensions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/geometry
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/geometry.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/geometry.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/geometry.source.tar.xz
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
%{_texmfdistdir}/tex/latex/geometry/geometry.sty
%doc %{_texmfdistdir}/doc/latex/geometry/README
%doc %{_texmfdistdir}/doc/latex/geometry/changes.txt
%doc %{_texmfdistdir}/doc/latex/geometry/geometry-samples.tex
%doc %{_texmfdistdir}/doc/latex/geometry/geometry.cfg
%doc %{_texmfdistdir}/doc/latex/geometry/geometry.pdf
#- source
%doc %{_texmfdistdir}/source/latex/geometry/geometry.drv
%doc %{_texmfdistdir}/source/latex/geometry/geometry.dtx
%doc %{_texmfdistdir}/source/latex/geometry/geometry.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 5.6-2
+ Revision: 752259
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 5.6-1
+ Revision: 718535
- texlive-geometry
- texlive-geometry
- texlive-geometry
- texlive-geometry

