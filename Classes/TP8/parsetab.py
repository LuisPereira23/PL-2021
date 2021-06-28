
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "id numComando : '?' idComando : '!' ExpComando : id '=' ExpComando : '!' '!'Exp : Exp '+' TermoExp : Exp '-' TermoExp : TermoTermo : Termo '*' FactorTermo : Termo '/' FactorTermo : FactorFactor : '(' Exp ')'Factor : numFactor : id"
    
_lr_action_items = {'?':([0,],[2,]),'!':([0,4,],[4,7,]),'id':([0,2,4,6,11,15,16,17,18,],[3,5,13,13,13,13,13,13,13,]),'$end':([1,5,7,8,9,10,12,13,14,20,21,22,23,24,],[0,-1,-4,-2,-7,-10,-12,-13,-3,-5,-6,-8,-9,-11,]),'=':([3,],[6,]),'(':([4,6,11,15,16,17,18,],[11,11,11,11,11,11,11,]),'num':([4,6,11,15,16,17,18,],[12,12,12,12,12,12,12,]),'+':([8,9,10,12,13,14,19,20,21,22,23,24,],[15,-7,-10,-12,-13,15,15,-5,-6,-8,-9,-11,]),'-':([8,9,10,12,13,14,19,20,21,22,23,24,],[16,-7,-10,-12,-13,16,16,-5,-6,-8,-9,-11,]),')':([9,10,12,13,19,20,21,22,23,24,],[-7,-10,-12,-13,24,-5,-6,-8,-9,-11,]),'*':([9,10,12,13,20,21,22,23,24,],[17,-10,-12,-13,17,17,-8,-9,-11,]),'/':([9,10,12,13,20,21,22,23,24,],[18,-10,-12,-13,18,18,-8,-9,-11,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Comando':([0,],[1,]),'Exp':([4,6,11,],[8,14,19,]),'Termo':([4,6,11,15,16,],[9,9,9,20,21,]),'Factor':([4,6,11,15,16,17,18,],[10,10,10,10,10,22,23,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Comando","S'",1,None,None,None),
  ('Comando -> ? id','Comando',2,'p_Comando_ler','calc_yacc.py',7),
  ('Comando -> ! Exp','Comando',2,'p_Comando_escrever','calc_yacc.py',12),
  ('Comando -> id = Exp','Comando',3,'p_Comando_atrib','calc_yacc.py',16),
  ('Comando -> ! !','Comando',2,'p_Comando_despejar','calc_yacc.py',20),
  ('Exp -> Exp + Termo','Exp',3,'p_Exp_add','calc_yacc.py',24),
  ('Exp -> Exp - Termo','Exp',3,'p_Exp_sub','calc_yacc.py',28),
  ('Exp -> Termo','Exp',1,'p_Exp_termo','calc_yacc.py',32),
  ('Termo -> Termo * Factor','Termo',3,'p_Termo_mul','calc_yacc.py',36),
  ('Termo -> Termo / Factor','Termo',3,'p_Termo_div','calc_yacc.py',40),
  ('Termo -> Factor','Termo',1,'p_Termo_factor','calc_yacc.py',48),
  ('Factor -> ( Exp )','Factor',3,'p_Factor_group','calc_yacc.py',52),
  ('Factor -> num','Factor',1,'p_Factor_num','calc_yacc.py',56),
  ('Factor -> id','Factor',1,'p_Factor_id','calc_yacc.py',60),
]
