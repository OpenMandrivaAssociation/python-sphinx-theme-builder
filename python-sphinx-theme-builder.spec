Name:		python-sphinx-theme-builder
Version:	0.2.0b2
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx_theme_builder/sphinx-theme-builder-%{version}.tar.gz
Summary:	A tool for authoring Sphinx themes with a simple (opinionated) workflow.
URL:		https://pypi.org/project/sphinx-theme-builder/
License:	GPL
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
A tool for authoring Sphinx themes with a simple (opinionated) workflow.

%files
%{_bindir}/stb
%{py_sitedir}/sphinx_theme_builder
%{py_sitedir}/sphinx_theme_builder-*.*-info
