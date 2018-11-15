.. title: Cloth Manipulation Using Random-Forest-Based Controller Parametrization
.. slug: robustm
.. date: 2017-09-15 10:00:00 UTC-03:00
.. tags: Robotics, Computer Vision, Machine Learning
.. author: Biao Jia
.. link:
.. description: 
.. category: 


Authors
=======
    * `Biao Jia <http://cs.unc.edu/~dm>`_, University of North Carolina at Chapel Hill
    * Zherong Pan, University of North Carolina at Chapel Hill
    * Zhe Hu, City University of Hong Kong
    * `Jia Pan <http://www.cityu.edu.hk/mbe/jiapan/>`_,  City University of Hong Kong
    * `Dinesh Manocha <http://cs.unc.edu/~dm>`_, University of North Carolina at Chapel Hill
    

Overview Video
==============
.. youtube:: iQu85o8lFjA 
   :align: center

ArXiv Report
============
	* https://arxiv.org/abs/1802.09661

Abstract
========

	* We present a novel approach for the manipulation of high-DOF deformable objects such as cloth. Our approach uses a random-forest-based controller that maps the observed visual features of the cloth to an optimal control action of the manipulator.  The topological structure of this random-forest-based controller is determined automatically based on the training data consisting of visual features and control actions.  This enables us to integrate the overall process of training data classification and controller optimization into an imitation learning (IL) algorithm.  Our approach enables joint feature extraction and controller optimization for cloth. We have evaluated our approach on different cloth manipulation benchmarks such as flattening, folding and twisting. In practice, our approach works well with deformable features learned based on the specific task. Moreover, our controller outperforms a simple or piecewise linear controller parametrization in terms of robustness to noise. In addition, our approach is easy to implement and does not require much parameter tuning.

Benchmarks
==========
.. youtube:: UIwLz47s2wM 
   :align: center

.. youtube:: qwvRgID08TY 
   :align: center


Related
============
	* `Manipulating Highly Deformable Materials Using a Visual Feedback Dictionary </clothm>`_
	* `GAMMA Group at UNC <http://gamma.cs.unc.edu/>`_



