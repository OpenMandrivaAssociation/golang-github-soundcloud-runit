%bcond_without check
%global goipath     github.com/soundcloud/go-runit
%global commit      06ad41a06c4a586951fb8040a697ecd39729640b

Version:            0

%global common_description %{expand:
Go library wrapping runit service status}

%gometa

Name:    %{goname}
Release: 0.2%{?dist}
Summary: Go library wrapping runit service status
License: MIT
URL:     %{gourl}
Source:  %{gosource}



%description
%{common_description}

%package   devel
Summary:   %{summary}
BuildArch: noarch

%description devel
%{common_description}

This package contains the source code needed for building packages that import
the %{goipath} Go namespace.

%prep
%gosetup -q
rm -rf vendor

%install
%goinstall

%check
%if %{with check}
  %gochecks
%endif

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git06ad41a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 17 2018 Paul Gier <pgier@redhat.com> - 0-0.1.20180517git06ad41a
- First package for Fedora
