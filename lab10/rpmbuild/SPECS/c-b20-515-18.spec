Name:       c-b20-515-18
Version:    1.0
Release:    1%{?dist}
Summary:    Программа студента Khraltsova Alexandra группы b20-515
Group:      Testing
License:    GPL
URL:        https://github.com/alexandrakhraltsova/OSS_LABS
Source:     %{name}-%{version}.tar.gz
BuildRequires: gcc

%global debug_package %{nil}

%description
A test package

%prep
%setup -q

%build
gcc -O2 -o c-b20-515-18-1 c-b20-515-18

%install
mkdir -p %{buildroot}%{_bindir}
cp c-b20-515-18 %{buildroot}%{_bindir}
sudo rpm -i ~/rpmbuild/RPMS/noarch/b20-515-17-1.0-1.el8.noarch.rpm --force

%files
%{_bindir}/c-b20-515-18

%changelog
* Wed May 24 2023 Khraltsova
- Added %{_bindir}/c-b20-515-18

