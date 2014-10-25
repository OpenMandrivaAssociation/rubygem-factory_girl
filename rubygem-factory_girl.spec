         
%define	rbname	factory_girl

Summary:	Framework and DSL for defining and using model instance factories
Name:		rubygem-%{rbname}

Version:	4.4.0
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://thoughtbot.com/projects/factory_girl
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
factory_girl provides a framework and DSL for defining and
using factories - less error-prone, more explicit, and
all-around easier to work with than fixtures.

%files
%{gem_dir}/gems/%{rbname}-%{version}/features/*
%{gem_dir}/gems/%{rbname}-%{version}/lib/*.rb
%{gem_dir}/gems/%{rbname}-%{version}/lib/factory_girl/*
%{gem_dir}/gems/%{rbname}-%{version}/spec/*
%{gem_dir}/specifications/%{rbname}-%{version}.gemspec
#-----------------------------------------------------

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%files doc
%doc %{gem_dir}/doc/%{rbname}-%{version}
#-----------------------------------------------------

%prep
%setup -q

%build
%gem_build -f '(features|spec)/'

%install
%gem_install









