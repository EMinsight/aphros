#!/usr/bin/env python3

import re
import os

text = '''<!--- Generated by [[GEN]] -->
<!--- DO NOT EDIT THIS FILE. Instead, edit and run [[GEN]]-->
# Aphrós

__SNSF scientific video competition__ until 31 March 2021:
&#x1f44d; [vote for our video "Foaming waterfall"](https://pollunit.com/polls/bestswisssciencevideo) &#x1f44d;

<img src="doc/images/foam.png" width=300 align="right">

Finite volume solver for incompressible multiphase flows with surface tension.

Key features:

- implementation in C++14
- scalability to thousands of compute nodes
- emulated coroutines for encapsulation in with block-wise processing
- fluid solver based on SIMPLE or Bell-Colella-Glaz methods
- advection with PLIC volume-of-fluid
- particle method for curvature estimation accurate at low resolutions
[[online demo]](https://cselab.github.io/aphros/curv.html)
[[ref:partstr]]
- scalable coalescence prevention
[[online demo]](https://cselab.github.io/aphros/wasm/hydro.html)
[[ref:pasc20]]
[[ref:multivof]]

## Online demos

[<img src="[[IMAGES]]/curv.png" height=200>](https://cselab.github.io/aphros/curv.html) | [<img src="[[IMAGES]]/wasm.png" height=200>](https://cselab.github.io/aphros/wasm/hydro.html) | [<img src="[[IMAGES]]/electrochem.png" height=200>](https://cselab.github.io/aphros/wasm/electrochem.html) | [<img src="[[IMAGES]]/aphros.png" width=200>](https://cselab.github.io/aphros/wasm/aphros.html)
:---:|:---:|:---:|:---:
curvature estimation | coalescence prevention | electrochemical reactor | complete solver

### Documentation

[Online version](<https://cselab.github.io/aphros/doc>) generated from [doc/sphinx](doc/sphinx).

### Requirements

C++14, CMake

Optional dependencies:
MPI,
parallel HDF5,
python3,
python3-numpy

Bundled optional dependencies:
[hypre](https://github.com/hypre-space/hypre),
[eigen](https://gitlab.com/libeigen/eigen),
[overlap](https://github.com/severinstrobl/overlap),
[vofi](https://github.com/VOFTracking/Vofi),
[fpzip](https://github.com/LLNL/fpzip)

### Clone and build

```
git clone https://github.com/cselab/aphros.git
```

First, follow [deploy/README.md](deploy/README.md) to
prepare environment and install dependencies. Then build with

```
cd src
make
```

### Docker

Instead of building the code in your system, you can build and run a Docker
container

```
docker build github.com/cselab/aphros --tag aphros
docker run -i aphros
```

### Minimal build without CMake

This is a minimal build without dependencies and tests.

```
cd src
APHROS_PREFIX=PREFIX make -f Makefile_legacy install
```
where `PREFIX` is the installation location (e.g. `~/.local`).

## Videos

Examples of simulations visualized using
[ParaView](https://www.paraview.org/) and [OSPRay](https://www.ospray.org/)
in collaboration with Jean M. Favre at [CSCS](https://www.cscs.ch).

|    |    |
:---:|:---:
[<img src="doc/images/coalescence.jpg" width=384>](https://www.youtube.com/watch?v=pRWGhGoQjyI) | [<img src="doc/images/taylor_green.jpg" width=250>]([[VIDEOS]]/taylor_green.mp4)
Coalescence of bubbles [[conf]](examples/202_coalescence) [[ref:partstr]] | Taylor-Green vortex with bubbles [[ref:pasc19]] [[ref:datadriven]]
[<img src="doc/images/vortex_bubble.jpg" width=200>]([[VIDEOS]]/vortex_bubble.mp4) | [<img src="doc/images/plunging_jet.jpg" width=200>]([[VIDEOS]]/plunging_jet.mp4)
Bubble trapped by vortex ring [[ref:datadriven]] | Plunging jet [[ref:pasc19]]
[<img src="doc/images/reactor.jpg" width=384>]([[VIDEOS]]/reactor.mp4) | [<img src="doc/images/mesh_bubbles.jpg" width=384>]([[VIDEOS]]/mesh_bubbles.mp4)
Electrochemical reactor [[ref:ees]] | Bubbles through mesh
[<img src="doc/images/rising_bubbles.jpg" width=384>](https://www.youtube.com/watch?v=WzOe0buD8uM) | [<img src="doc/images/foaming_waterfall.jpg" width=384>](https://www.youtube.com/watch?v=0Cj8pPYNJGY)
 Clustering of bubbles [[conf]](examples/205_multivof/clustering) [[ref:aps]] [[ref:cscs]] [[ref:multivof]] | Foaming waterfall [[conf]](examples/205_multivof/waterfall) [[ref:pasc20]] [[ref:multivof]] [[vote &#x1f44d;]](https://pollunit.com/polls/bestswisssciencevideo)

|     |
|:---:|
|[<img src="doc/images/breaking_waves.jpg" width=795>](https://www.youtube.com/watch?v=iGdphpztCJQ)|
|APS Gallery of Fluid Motion 2019 award winner: Breaking waves: to foam or not to foam? [[ref:aps]]|

## Developers

Aphros is developed and maintained by researchers at ETH Zurich

* [Petr Karnakov](https://www.cse-lab.ethz.ch/member/petr-karnakov/)
* [Dr. Sergey Litvinov](https://www.cse-lab.ethz.ch/member/sergey-litvinov/)
* [Dr. Fabian Wermelinger](https://www.cse-lab.ethz.ch/member/fabian-wermelinger/)

under the supervision of

* [Prof. Petros Koumoutsakos](https://www.cse-lab.ethz.ch/member/petros-koumoutsakos/)

## Publications

[[item:ees]] S. M. H. Hashemi, P. Karnakov, P. Hadikhani, E. Chinello, S.
  Litvinov, C.  Moser, P. Koumoutsakos, and D. Psaltis, "A versatile and
  membrane-less electrochemical reactor for the electrolysis of water and
  brine", _Energy & environmental science_, 2019
  [10.1039/C9EE00219G](https://doi.org/10.1039/C9EE00219G)
[[item:pasc19]] P. Karnakov, F. Wermelinger, M. Chatzimanolakis, S. Litvinov,
  and P.  Koumoutsakos, "A high performance computing framework for multiphase,
  turbulent flows on structured grids" in _Proceedings of the platform for
  advanced scientific computing conference on – PASC ’19_, 2019
  [10.1145/3324989.3325727](https://doi.org/10.1145/3324989.3325727)
  [[pdf]]([[PDF]]/pasc2019.pdf)
[[item:icmf]] P. Karnakov, S. Litvinov, P. Koumoutsakos
  "Coalescence and transport of bubbles and drops"
  _10th International Conference on Multiphase Flow (ICMF)_, 2019
  [[pdf]]([[PDF]]/icmf2019.pdf)
[[item:partstr]] P. Karnakov, S. Litvinov, and P. Koumoutsakos, "A hybrid
  particle volume-of-fluid method for curvature estimation in multiphase
  flows”, _International journal of multiphase flow_, 2020
  [10.1016/j.ijmultiphaseflow.2020.103209](https://doi.org/10.1016/j.ijmultiphaseflow.2020.103209)
  [arXiv:1906.00314](https://arxiv.org/abs/1906.00314)
[[item:datadriven]] Z. Wan, P. Karnakov, P. Koumoutsakos, T. Sapsis, "Bubbles in
  Turbulent Flows: Data-driven, kinematic models with history terms”,
  _International journal of multiphase flow_, 2020
  [10.1016/j.ijmultiphaseflow.2020.103286](https://doi.org/10.1016/j.ijmultiphaseflow.2020.103286)
  [arXiv:1910.02068](https://arxiv.org/abs/1910.02068)
[[item:aps]] P. Karnakov, S. Litvinov, J. M. Favre, P. Koumoutsakos
  "V0018: Breaking waves: to foam or not to foam?"
  _Gallery of Fluid Motion Award_
  [10.1103/APS.DFD.2019.GFM.V0018](https://doi.org/10.1103/APS.DFD.2019.GFM.V0018)
[[item:cscs]] Annual report 2019 of the Swiss National Supercomputing Centre (cover page)
  [[link]](https://www.cscs.ch/publications/annual-reports/cscs-annual-report-2019)
[[item:pasc20]] P. Karnakov, F. Wermelinger, S. Litvinov,
  and P.  Koumoutsakos, "Aphros: High Performance Software for Multiphase Flows with Large Scale
  Bubble and Drop Clusters" in _Proceedings of the platform for
  advanced scientific computing conference on – PASC ’20_, 2020
  [10.1145/3394277.3401856](https://doi.org/10.1145/3394277.3401856)
  [[pdf]]([[PDF]]/pasc2020.pdf)
[[item:multivof]] P. Karnakov, S. Litvinov, P. Koumoutsakos
"Computing foaming flows across scales: from breaking waves to microfluidics", 2021
[arXiv:2103.01513](https://arxiv.org/abs/2103.01513)
'''

m_refs = list(re.finditer("\[\[ref:[^]]*\]\]", text))
m_items = list(re.finditer("\[\[item:[^]]*\]\]", text))
refs = [m_ref.group(0) for m_ref in m_refs]

gen = text
gen = gen.replace('[[GEN]]', os.path.basename(__file__))
gen = gen.replace('[[VIDEOS]]', "https://cselab.github.io/aphros/videos")
gen = gen.replace('[[IMAGES]]', "https://cselab.github.io/aphros/images")
gen = gen.replace('[[PDF]]', "https://cselab.github.io/aphros/pdf")
found_refs = set()
for i, m_item in enumerate(m_items):
    item = m_item.group(0)
    name = re.match("\[\[item:([^]]*)\]\]", item).group(1)
    start = m_item.start(0)
    end = m_items[i + 1].start(0) if i + 1 < len(m_items) else len(text)
    m_url = re.search("\((http[^)]*)\)", text[start:end])
    ref = "[[ref:{}]]".format(name)
    found_refs.add(ref)

    gen = gen.replace(item, "{:}.".format(i + 1))

    if m_url:
        url = m_url.group(1)
        gen = gen.replace(ref, "[[{:}]]({})".format(i + 1, url))
    else:
        if ref in refs:
            print("Warning: no URL found for '{}'".format(item))
        gen = gen.replace(ref, "[{:}]".format(i + 1))

unknown_refs = set(refs) - found_refs
if len(unknown_refs):
    for ref in unknown_refs:
        print("Warning: item not found for '{}'".format(ref))

with open("README.md", 'w') as f:
    f.write(gen)
