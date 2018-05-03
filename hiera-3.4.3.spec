%define _prefix /opt/freeware
%define _rubybin /opt/freeware/bin/ruby
%define _defaultdocdir %{_prefix}/doc
%define tarballname hiera

%{!?ruby_sitelibdir: %define ruby_sitelibdir %(%{_rubybin} -rrbconfig -e 'puts RbConfig::CONFIG["sitelibdir"]')}

Name:           hiera
Version:        3.4.3
Release:        1
Summary:        Hierarchical database lookup tool
License:        ASL 2.0
URL:            http://puppetlabs.com
Source0:        %{tarballname}-%{version}.tar.gz
Group:          System Environment/Base
BuildRoot:      %{_tmppath}/%{tarballname}-%{version}-%{release}-%(%{__id_u} -n)
Requires:       ruby = 2.4.0
Requires:       facter
Provides:       hiera-3.4.3

%description
Puppet lets you centrally manage every important aspect of your system using a
cross-platform specification language that manages all the separate elements
normally aggregated in different files, like users, cron jobs, and hosts,
along with obviously discrete elements like packages, services, and files.

%prep
%setup -q -n %{tarballname}-%{version}


%build

find examples/ -type f -empty | xargs rm
find examples/ -type f | xargs chmod a-x

%install
rm -rf %{buildroot}
mkdir -p $RPM_BUILD_ROOT/%{_sharedstatedir}/hiera
%{_rubybin} install.rb --destdir=%{buildroot} --configdir=%{_sysconfdir} --configs

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/hiera
%{ruby_sitelibdir}/hiera.rb
%{ruby_sitelibdir}/hiera
%config(noreplace) %{_sysconfdir}/hiera.yaml
%{_sharedstatedir}/hiera
%doc COPYING README.md

%changelog
* Thu May 03 2018 Rogerio Goncalves <rogerlz@gmail.com>
- updated for hiera 3.4.3.
* Tue Nov 03 2015 Bill Wilcox <bwilcox@4ied.net>
- Build of hiera 3.0.1
* Mon Dec 23 2013 Bill Wilcox <bwilcox@4ied.net>
- Build of hiera 1.3.1-rc1

