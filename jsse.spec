%define		_ver	03
Summary:	Java Secure Socket Extension
Summary(pl.UTF-8):	Rozszerzenie Secure Socket do Javy
Name:		jsse
Version:	1.0.3_%{_ver}
Release:	1
License:	restricted, non-distributable (see COPYRIGHT.html)
Group:		Development/Languages/Java
Source0:	%{name}-1_0_3_%{_ver}-gl.zip
URL:		http://java.sun.com/products/jsse/
NoSource:	0
Requires:	jre >= 1.2.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	%{_datadir}/java

%description
Java Secure Socket Extension.

%description -l pl.UTF-8
Rozszerzenie Java Secure Socket Extension do Javy.

%package doc
Summary:	Documentation for Java Secure Socket Extension
Summary(pl.UTF-8):	Dokumentacja do Java Secure Socket Extension
Group:		Development/Languages/Java

%description doc
Documentation for Java Secure Socket Extension.

%description doc -l pl.UTF-8
Dokumentacja do rozszerzenia Java Secure Socket Extension.

%prep
%setup -q -n %{name}%{version}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_javalibdir}
install lib/*.jar $RPM_BUILD_ROOT%{_javalibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt *.html
%{_javalibdir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc doc/*
