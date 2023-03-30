%global octpkg psychrometrics

Summary:	A toolbox for air-water vapor psychrometrics for GNU Octave
Name:		octave-psychrometrics
Version:	0.2.1
Release:	1
License:	GPLv3+
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/psychrometrics/
Url:		https://github.com/aumpierre-unb/Psychrometrics-for-GNU-Octave/
Source0:	https://github.com/aumpierre-unb/Psychrometrics-for-GNU-Octave/archive/v%{version}/psychrometrics-%{version}.tar.gz

BuildRequires:  octave-devel >= 4.0.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

BuildArch:	noarch

%description
A toolbox for air-water vapor psychrometrics for GNU Octave.

%files
%license COPYING
%doc NEWS README.md
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n Psychrometrics-for-GNU-Octave-%{version}

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

