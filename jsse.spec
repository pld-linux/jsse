Summary:	Java Secure Socket Extension
Summary(pl):	Rozszerzenie Secure Socket do Javy
Name:		jsse
Version:	1.0.2
Release:	1
License:	See http://java.sun.com/products/jsse for details!!!
Group:		Development/Languages/Java
Group(de):	Entwicklung/Sprachen/Java
Group(pl):	Programowanie/Jêzyki/Java
Source0:	jsse-1_0_2-gl.zip
URL:		http://java.sun.com/products/jsse/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java

%description
Java Secure Socket Extension.

%description -l pl
Rozszerzenie Java Secure Socket Extension do Javy.

%package doc
Summary:	Documentation for Java Secure Socket Extension
Summary(pl):	Dokumentacja do Java Secure Socket Extension
Group:		Development/Languages/Java
Group(de):	Entwicklung/Sprachen/Java
Group(pl):	Programowanie/Jêzyki/Java

%description doc
Documentation for Java Secure Socket Extension.

%description doc -l pl
Dokumentacja do rozszerzenia Java Secure Socket Extension.

%prep
%setup -q -n %{name}%{version}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_javalibdir}
install lib/*.jar $RPM_BUILD_ROOT%{_javalibdir}

gzip -9nf *.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz *.html
%{_javalibdir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc doc/*
