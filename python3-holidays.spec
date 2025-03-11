# Conditional build:
%bcond_with	doc	# API documentation
%bcond_with	tests	# unit tests

%define		module	holidays
Summary:	Generate and work with holidays in Python
Name:		python3-%{module}
Version:	0.49
Release:	3
License:	MIT
Group:		Libraries/Python
Source0:	https://pypi.debian.net/holidays/%{module}-%{version}.tar.gz
# Source0-md5:	b5271a3bd5df59ed3e378718597aff31
URL:		https://github.com/vacanza/python-holidays
BuildRequires:	python3-modules >= 1:3.8
%if %{with tests}
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python3-tox
%endif
Requires:	python3-modules >= 1:3.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A fast, efficient Python library for generating country- and
subdivision- (e.g. state or province) specific sets of
government-designated holidays on the fly. It aims to make determining
whether a specific date is a holiday as fast and flexible as possible.

%package apidocs
Summary:	API documentation for Python %{module} module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona %{module}
Group:		Documentation

%description apidocs
API documentation for Python %{module} module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona %{module}.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%if %{with doc}
%{_bindir}/tox -e docs
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CONTRIBUTING.rst README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/*
%endif
