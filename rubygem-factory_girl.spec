# Generated from factory_girl-1.3.3.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	factory_girl

Summary:	Framework and DSL for defining and using model instance factories
Name:		rubygem-%{rbname}

Version:	4.4.0
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://thoughtbot.com/projects/factory_girl
Source0:	http://rubygems.org/gems/factory_girl-4.4.0.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
factory_girl provides a framework and DSL for defining and
using factories - less error-prone, more explicit, and
all-around easier to work with than fixtures.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build -f '(features|spec)/'

%install
%gem_install

%clean

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
# %dir %{ruby_gemdir}/gems/%{rbname}-%{version}/features
# %{ruby_gemdir}/gems/%{rbname}-%{version}/features/*
# %dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
# %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
# %dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/factory_girl
# %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/factory_girl/*
# %dir %{ruby_gemdir}/gems/%{rbname}-%{version}/spec
# %{ruby_gemdir}/gems/%{rbname}-%{version}/spec/*
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/*.rdoc
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}
