%bcond_with bootstrap
%global packname  relations
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.6
Release:          3
Summary:          Data Structures and Algorithms for Relations
Group:            Sciences/Mathematics
License:          GPL-2
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
Requires:         R-sets R-cluster R-stats R-slam R-Rgraphviz
Requires:         R-Rglpk R-lpSolve R-Rsymphony 
%if %{without bootstrap}
Requires:         R-clue
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-sets R-cluster R-stats R-slam R-Rgraphviz
BuildRequires:    R-Rglpk R-lpSolve R-Rsymphony 
%if %{without bootstrap}
BuildRequires:    R-clue
%endif

%define debug_package %{nil}

%description
Data structures and algorithms for k-ary relations with arbitrary domains,
featuring relational algebra, predicate functions, and fitters for
consensus relations.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/po
