Summary:	Java Secure Socket Extension
Name:		jsse
Version:	1.0.2
Release:	1
License:	See http://java.sun.com/products/jsse for details!!!
Group:		Development/Languages/Java
Group(de):	Entwicklung/Sprachen/Java
Group(pl):	Programowanie/Jêzyki/Java
Source0:	jsse-1_0_2-gl.zip
URL:		http://java.sun.com/products/jsse
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java

%description
Java Secure Socket Extension

%package doc
Group:		Development/Languages/Java
Group(de):	Entwicklung/Sprachen/Java
Group(pl):	Programowanie/Jêzyki/Java
Summary:	Documentation for Java Secure Socket Extension

%description doc
Documentation for Java Secure Socket Extension

%prep
%setup -q -n %{name}%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_javalibdir}
cp lib/*.jar $RPM_BUILD_ROOT/%{_javalibdir}

gzip -9nf *.html *.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%dir %{_javalibdir}
%{_javalibdir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc doc/*
