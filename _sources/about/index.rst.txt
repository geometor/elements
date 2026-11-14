:navigation: header
:order: 10
:nav_title: About

.. _about:
.. _about-index:
.. _about-elements:

About
=====

.. rubric:: Extracting Historical Semantic Knowledge & Repurposing It for Exact Symbolic Reasoning

About This Edition
------------------

**GEOMETOR • elements** is the computable G-Index compilation layer and symbolic dependency mapping engine for **Euclid of Alexandria's** *Elements* (c. 300 BCE). Created and maintained by **phi ARCHITECT**, the edition sequences the definitions, postulates, common notions, and propositions across all thirteen books into a computable directed acyclic graph (DAG) spanning **G.1 through G.601**. By mapping every theorem back to its axiomatic roots, the repository recovers the transparent genealogy of deductive truth underpinning the foundation of mathematics.

Each node in the G-Index is extracted into machine-addressable semantic elements presented through a synchronized four-track Book Codex:
1. **Pseudocode Track**: Enunciations tightened into formal, fact-oriented mathematical specifications, explicit ``given`` / ``construct`` / ``prove`` signatures, interactive vector diagrams, and step-by-step deductive chains with explicit ``∵ G.<k>`` justification links.
2. **Video Track**: High-definition animated construction playbacks dynamically unveiling geometric derivations.
3. **Code Track**: Standalone, reproducible Python builder functions executing on :mod:`geometor.model` and `SymPy <https://www.sympy.org>`_, accompanied by proposition-specific dependency DAG subgraphs.
4. **Heath Track**: Sir Thomas Little Heath's definitive English translation (Cambridge, 1908) enriched with GEOMETOR symbolic indicators and deep bi-directional links.

Within the GEOMETOR Digital Scriptorium, ``geometor.elements`` serves as the central computational grammar connecting historical treatises to modern symbolic geometry. It acts as the algorithmic twin to ``geometor.euclid``, which preserves the unabridged three-volume historical apparatus and manuscript folios. In turn, it feeds computable axiomatic constructions directly into the golden ratio discovery canon ``geometor.divine``, Luca Pacioli's ``geometor.pacioli`` (*De Divina Proportione*), and Albrecht Dürer's ``geometor.durer`` (*Underweysung der Messung*).

The GEOMETOR Mission
--------------------

Founded by **phi ARCHITECT**, the GEOMETOR project is dedicated to three foundational pillars:

Extracting Historical Semantic Knowledge
    Moving beyond passive page scans and OCR to recover the living deductive structure of 2,300+ years of geometric, axiomatic, and philosophical treatises. GEOMETOR elevates prose, marginal citations, primary-source folios (via ``publish folio``), and calibrated Ink-to-Vector ``.euclid-graphic`` diagrams into structured, machine-addressable semantic graphs.

Exact Symbolic Grounding (``geometor.model``)
    Anchoring geometric constructions in 100% exact symbolic algebra (`SymPy <https://www.sympy.org>`_) and Rational Trigonometry invariants (quadrance, spread, cross-ratio) over exact algebraic number fields rather than floating-point approximations. Every geometric theorem and construction is mathematically verified and permanently reproducible.

Repurposing Knowledge Across Mediums
    Re-deploying extracted semantic and algebraic structures across synchronized multi-track **Book Codices** and EPUB 3 editions (``photon-platform/publish``), computable deductive canons (``geometor.elements``, ``geometor.etc``, ``geometor.pappus``, ``geometor.divine``), interactive SVG laboratories (``geometor.explorer``), QHD visual broadcasts, and neuro-symbolic program synthesis (``geometor.seer``) across `geometor.com <https://geometor.com>`_.

Sources, Provenance & Methodology
---------------------------------

The G-Index formalization and textual apparatus are grounded in authoritative historical witnesses and critical scholarship:

- **Primary Translation & Commentary**: Sir Thomas Little Heath, *The Thirteen Books of Euclid's Elements*, 3 vols. (Cambridge University Press, 1908; 2nd ed. 1926; Dover Publications reprint).
- **Greek Critical Text**: Johan Ludvig Heiberg, *Euclidis Elementa*, 5 vols. in *Euclidis Opera Omnia* (Leipzig: B.G. Teubner, 1883–1888).
- **Archival Manuscript Witnesses**: Collation against *Codex Vaticanus Graecus 190* (Vatican Library, 10th c.) and *Codex Bodleianus MS. D'Orville 301* (Bodleian Library, Oxford, copied 888 CE by Stephen the Clerk).
- **Ancient Commentators**: Proclus Diadochus (*Commentary on the First Book of Euclid's Elements*), Pappus of Alexandria (*Collection*, Book VII), and Hero of Alexandria.
- **Digital Scriptorium Methodology**: Every proposition is codified into a formal algebraic pipeline within :mod:`geometor.elements`, generating interactive SVG graphics, complete dependency trees, and executable verification suites compiled via the Photon Publisher framework.
