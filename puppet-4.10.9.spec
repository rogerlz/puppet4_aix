%define _prefix /opt
%define _rubybin /opt/freeware/bin/ruby
%define _defaultdocdir %{_prefix}/doc
%define tarballname puppet

%{!?ruby_sitelibdir: %global ruby_sitelibdir %(%{_rubybin} -rrbconfig -e 'puts RbConfig::CONFIG["sitelibdir"]')}
%global confdir conf/redhat

Name:           puppet
Version:        4.10.9
Release:        1
Summary:        A network tool for managing many disparate systems
License:        ASL 2.0
URL:            http://puppetlabs.com
Source0:        %{name}-%{version}.tar.gz
Group:          System Environment/Base
BuildRoot:      %{_tmppath}/%{tarballname}-%{version}-%{release}-%(%{__id_u} -n)
Requires:       ruby = 2.4.0
Requires:       facter >= 2.5.1
Buildrequires:  facter >= 2.5.1
Provides:       puppet

%description
Puppet lets you centrally manage every important aspect of your system using a
cross-platform specification language that manages all the separate elements
normally aggregated in different files, like users, cron jobs, and hosts,
along with obviously discrete elements like packages, services, and files.

%prep
rm -rf %{_builddir}/%{name}-%{version}-root
%setup -n %{tarballname}-%{version}

%build

%install
cd %{_builddir}/%{name}-%{version}
%{_rubybin} install.rb --destdir=%{buildroot} --vardir=%{buildroot}/opt/puppetlabs/puppet/cache --quick

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_prefix}/freeware/bin
#%{_bindir}/puppet
%{ruby_sitelibdir}/*.rb
%{ruby_sitelibdir}/puppet
%{ruby_sitelibdir}/hiera
%{_prefix}/puppetlabs
%{_prefix}/freeware/share/man
%doc
/var/log
/var/run
/etc/puppetlabs

%changelog
* Thu May 03 2018 Rogerio Goncalves <rogerlz@gmail.com>
- updated for facter 4.10.9.
* Tue Nov 03 2015 Bill Wilcox <bwilcox@4ied.net>
- Build of puppet 4.2.3
* Tue Mar 18 2014 Bill Wilcox <bwilcox@4ied.net>
- Build of puppet 3.4.3
* Mon Dec 23 2013 Bill Wilcox <bwilcox@4ied.net>
- Build of puppet 3.2.2
* Thu Nov 27 2013 Bill Wilcox <bwilcox@4ied.net>
- Build of puppet-local 2.7.22-2.local
* Thu Jul 18 2013 Bill Wilcox <bwilcox@4ied.net>
- Build of puppet-local 2.7.22-1.local
* Tue Feb 12 2013 Bill Wilcox <bwilcox@4ied.net>
- Build of puppet-local 2.7.20-1.local
* Mon Dec 19 2011 Nick Bausch <nick.bausch@gmail.com> - 2.7.6-1.local
- First puppet-local build for AIX

