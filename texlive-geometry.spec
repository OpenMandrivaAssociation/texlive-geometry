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
Requires(pre):	texlive-tlpkg
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

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/geometry
%dir %{_datadir}/texmf-dist/source/latex/geometry
%dir %{_datadir}/texmf-dist/tex/latex/geometry
%doc %{_datadir}/texmf-dist/doc/latex/geometry/README.md
%doc %{_datadir}/texmf-dist/doc/latex/geometry/changes.txt
%doc %{_datadir}/texmf-dist/doc/latex/geometry/geometry-de.pdf
%doc %{_datadir}/texmf-dist/doc/latex/geometry/geometry-samples-de.tex
%doc %{_datadir}/texmf-dist/doc/latex/geometry/geometry-samples.tex
%doc %{_datadir}/texmf-dist/doc/latex/geometry/geometry.cfg
%doc %{_datadir}/texmf-dist/doc/latex/geometry/geometry.pdf
%doc %{_datadir}/texmf-dist/source/latex/geometry/geometry-de.drv
%doc %{_datadir}/texmf-dist/source/latex/geometry/geometry-de.dtx
%doc %{_datadir}/texmf-dist/source/latex/geometry/geometry-de.ins
%doc %{_datadir}/texmf-dist/source/latex/geometry/geometry.dtx
%{_datadir}/texmf-dist/tex/latex/geometry/geometry.sty
