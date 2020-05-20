""" 
A short segment of code to be implemented within the
ARES (https://ares.readthedocs.io/en/latest/index.html)
code to account for interacting dark matter

NOT Completed, project put off until later time as per
suggestion from Prof. Gluscevic

Author: Karime Maamari
Date: 10/2019

"""
import os
import numpy as np
from scipy.misc import derivative
from scipy.optimize import fsolve
from scipy.integrate import quad, ode
from ..util.Math import interp1d
from ..util.ReadData import _load_inits
from ..util.ParameterFile import ParameterFile
from ..util.ParameterBundles import ParameterBundle
from .Constants import c, G, km_per_mpc, m_H, m_He, sigma_SB, g_per_msun, \
    cm_per_mpc, cm_per_kpc, k_B, m_p

##############################################################################################################################

	# Import relevant constants
		from Constants import m_e, m_H, sigma_T,
	
	# Variables:
		"""
		params:
			m_e, m_H, sigma_T - imported
			*Tb, Tx - to be imported
			*m_x, sigma_0, sigma_He, mu_b, rho_x (possibly rho_m_z0?), c_n - nope
			rho_gamma (rho_cdm_z0), rho_b (rho_b_z0), Tgamma (TCMB), n_e (n_e), H (hubble_0) - set above
			a, sigma_0 - set below
		"""
		self.rho_x = # ?
       self.sigma_He =  # ??
       self.m_x =   # DM Mass?
		self.mu_b =  # Mean molecular weight
       self.c_n =   # Thermalization rate coefficients
	
        def scale_factor(z):
			return 1/1+z
        self.sigma_0 = 1e-20 # ??

	# DVORKIN EVOLUTIONS:
		# Dvorkin paper - https://arxiv.org/pdf/1311.2937.pdf
        
		# Baryonic temperature evolution
        def dotTb(H, Tb, mu_b, m_x, m_H, Tx, rho_x, rho_b, m_e, Tgamma):
			# Thermalizations      
        	F_He = 1+0.24*((sigma_He/sigma_0)-1)
        	f_He = 0.24 	
			R_gamma = (4/3)*(rho_gamma/rho_b)*a*n_e*sigma_T
			Rprime_x = R_x*(1+(3/(m_x+4*m_H))*(((1-f_He)/F_He)-1))
			
			return -2*H*Tb+\
					((2*mu_b)/(m_x+m_H))*Rprime_x*(Tx-Tb)*(rho_x/rho_b)+\
					((2*mu_b)/m_e)*R_gamma*(Tgamma-Tb)
       
		# DM temperature evolution		
		def dotTx(H, Tx, m_x, m_H, Tb):
			# Thermalization
			F_He = 1+0.24*((sigma_He/sigma_0)-1)
        	f_He = 0.24 
			Rprime_x = R_x*(1+(3/(m_x+4*m_H))*(((1-f_He)/F_He)-1))			

			return -2*H*Tx+\
			((2*m_x)/(m_x+m_H))*Rprime_x*(Tb-Tx)

    # MUNOZ EVOLUTIONS:
        # Munoz paper - https://arxiv.org/pdf/1708.08923.pdf
        # For variables - https://arxiv.org/pdf/astro-ph/9506072.pdf

        # Baryonic temperature evolution
        def dotTb(H,Tb,T_gamma,Tx,dotQ_ph):
			# Thermalizations
		   	gamma_c = (8*mu*rho_Gamma*n_e*sigma_T)/(3*m_e*rho_B)  # Compton thermalization
			gamma_xb = ((rho_x*mu_b*sigma_n)/((m_x+m_b)**2))*(((Tb/m_b)+(Tx/m_x))**((n+1)/2))*\	# Baryonic thermalization
						((2**((5+n)/2)*gamma(3+(n/2)))/math.sqrt(math.pi))
           dotQ_ph = # Photoheating term - can be obtained from CUBA code as per Munoz paper

           return (-2*H*Tb+
                    gamma_c*(T_gamma-Tb)) +\
                    ((2/3)*gamma_xb*(Tx - Tb)) +\
                    +((2/3)*dotQ_ph)

        # DM temperature evolution
        def dotTx(H,Tx,Tb):
			# Thermalizations
			gamma_xb = # ??

           return (-2*H*Tx) +\
                   ((2/3)*gamma_xb*(Tb-Tx))
    ##############################################################################################################################

