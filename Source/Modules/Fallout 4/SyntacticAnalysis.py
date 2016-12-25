import os, sys
PYTHON_VERSION = sys.version_info
if PYTHON_VERSION[0] == 2:
	import imp
	root, module = os.path.split(os.getcwd())

	lexicalModule = os.path.join(root, module, "LexicalAnalysis.py")
	imp.load_source("LexicalAnalysis", lexicalModule)

	from LexicalAnalysis import *

	# Cleaning up
	del root
	del module
	del coreModule
	del lexicalModule
elif PYTHON_VERSION[0] >= 3:
	from .LexicalAnalysis import *

# It is faster to store Statement/Node type as an attribute in a Statement object than it is to use the isinstance() function.
class StatementEnum(object):
	ASSIGNMENT = 0
	CUSTOMEVENT = 1
	DOCSTRING = 2
	ELSE = 3
	ELSEIF = 4
	ENDEVENT = 5
	ENDFUNCTION = 6
	ENDGROUP = 7
	ENDIF = 8
	ENDPROPERTY = 9
	ENDSTATE = 10
	ENDSTRUCT = 11
	ENDWHILE = 12
	EVENTSIGNATURE = 13
	EXPRESSION = 14
	FUNCTIONSIGNATURE = 15
	GROUPSIGNATURE = 16
	IF = 17
	IMPORT = 18
	PARAMETER = 19
	PROPERTYSIGNATURE = 20
	RETURN = 21
	SCRIPTSIGNATURE = 22
	STATESIGNATURE = 23
	STRUCTSIGNATURE = 24
	VARIABLE = 25
	WHILE = 26
	#Caprica extensions
	BREAK = 27
	CONTINUE = 28
	SWITCH = 29
	CASE = 30
	DEFAULT = 31
	ENDSWITCH = 32
	FOR = 33
	ENDFOR = 34
	FOREACH = 35
	ENDFOREACH = 36
	DO = 37
	LOOPWHILE = 38

StatementDescription = [
	"ASSIGNMENT",
	"CUSTOMEVENT",
	"DOCSTRING",
	"ELSE",
	"ELSEIF",
	"ENDEVENT",
	"ENDFUNCTION",
	"ENDGROUP",
	"ENDIF",
	"ENDPROPERTY",
	"ENDSTATE",
	"ENDSTRUCT",
	"ENDWHILE",
	"EVENTSIGNATURE",
	"EXPRESSION",
	"FUNCTIONSIGNATURE",
	"GROUPSIGNATURE",
	"IF",
	"IMPORT",
	"PARAMETER",
	"PROPERTYSIGNATURE",
	"RETURN",
	"SCRIPTSIGNATURE",
	"STATESIGNATURE",
	"STRUCTSIGNATURE",
	"VARIABLE",
	"WHILE",
	#Caprica extensions
	"BREAK",
	"CONTINUE",
	"SWITCH",
	"CASE",
	"DEFAULT",
	"ENDSWITCH",
	"FOR",
	"ENDFOR",
	"FOREACH",
	"ENDFOREACH",
	"DO",
	"LOOPWHILE"
]

class NodeEnum(object):
	ARRAYATOM = 0
	ARRAYCREATION = 1
	ARRAYFUNCORID = 2
	BINARYOPERATOR = 3
	CONSTANT = 4
	EXPRESSION = 5
	FUNCTIONCALL = 6
	FUNCTIONCALLARGUMENT = 7
	IDENTIFIER = 8
	LENGTH = 9
	STRUCTCREATION = 10
	UNARYOPERATOR = 11

NodeDescription = [
	"ARRAYATOM",
	"ARRAYCREATION",
	"ARRAYFUNCORID",
	"BINARYOPERATOR",
	"CONSTANT",
	"EXPRESSION",
	"FUNCTIONCALL",
	"FUNCTIONCALLARGUMENT",
	"IDENTIFIER",
	"LENGTH",
	"STRUCTCREATION",
	"UNARYOPERATOR"
]

class Identifier(object):
	__slots__ = [
		"namespace", # list of str
		"name", # str
	]

	def __init__(self, aIdentifier):
		assert isinstance(aIdentifier, list #Prune
		self.name = aIdentifier.pop()
		self.namespace = aIdentifier

class Type(object):
	__slots__ = [
		"identifier", # Identifier
		"isArray", # bool
		"isStruct" # bool
	]

	def __init__(self, aIdentifier, aArray, aStruct):
		assert isinstance(aIdentifier, Identifier) #Prune
		assert isinstance(aArray, bool) #Prune
		assert isinstance(aStruct, bool) #Prune
		self.identifier = aIdentifier
		self.isArray = aArray
		self.isStruct = aStruct

class Node(object):
	__slots__ = []

	def __init__(self):
		pass

class ArrayAtomNode(Node):
	__slots__ = [
		"child", # *Node
		"expression" # *Node
	]

	def __init__(self, aChild, aExpression):
		assert isinstance(aChild, Node) #Prune
		assert isinstance(aExpression, Node) #Prune
		self.child = aChild
		self.expression = aExpression

class ArrayCreationNode(Node):
	__slots__ = [
		""
	]

	def __init__(self):
		pass

class ArrayFuncOrIdNode(Node):
	__slots__ = [
		"child", # *Node
		"expression" # *Node
	]

	def __init__(self, aChild, aExpression):
		assert isinstance(aChild, Node) #Prune
		assert isinstance(aExpression, Node) #Prune
		self.child = aChild
		self.expression = aExpression

class BinaryOperatorNode(Node):
	__slots__ = [
		"operator", # Token
		"leftOperand", # *Node
		"rightOperand", # *Node
	]

	def __init__(self, aOperator, aLeftOperand, aRightOperand):
		assert isinstance(aOperator, Token) #Prune
		assert isinstance(aLeftOperand, Node) #Prune
		assert isinstance(aRightOperand, Node) #Prune
		self.operator = aOperator
		self.leftOperand = aLeftOperand
		self.rightOperand = aRightOperand

class ConstantNode(Node):
	__slots__ = [
		"value" # Token
	]

	def __init__(self, aValue):
		assert isinstance(aValue, Token) #Prune
		self.value = aValue

class ExpressionNode(Node):
	__slots__ = [
		"child", # *Node
	]

	def __init__(self, aChild):
		assert isinstance(aChild, Node) #Prune
		self.child = aChild

class FunctionCallArgumentNode(Node):
	__slots__ = [
		"identifier", # Identifier (optional)
		"value" # Expression
	]

	def __init__(self, aIdentifier, aValue):
		if aIdentifier: #Prune
			assert isinstance(aIdentifier, Identifier) #Prune
		assert isinstance(aValue, Expression) #Prune
		self.identifier = aIdentifier
		self.value = aValue

class FunctionCallNode(Node):
	__slots__ = [
		"identifier", # Identifier
		"arguments" # list of FunctionCallArgumentNode
	]

	def __init__(self, aIdentifier, aArguments):
		assert isinstance(aIdentifier, Identifier) #Prune
		assert isinstance(aArguments, list) #Prune
		self.identifier = aIdentifier
		self.arguments = aArguments

class IdentifierNode(Node):
	__slots__ = [
		"identifier" # Identifier
	]

	def __init__(self, aIdentifier):
		assert isinstance(aIdentifier, Identifier) #Prune
		self.identifier = aIdentifier

class LengthNode(Node):
	__slots__ = []

	def __init__(self):
		pass

class StructCreationNode(Node):
	__slots__ = [
		"identifier" # Identifier
	]

	def __init__(self, aIdentifier):
		assert isinstance(aIdentifier, Identifier) #Prune
		self.identifier = aIdentifier

class UnaryOperatorNode(Node):
	__slots__ = [
		"operator", # Token
		"operand" # *Node
	]

	def __init__(self, aOperator, aOperand):
		assert isinstance(aOperator, Token) #Prune
		assert isinstance(aOperand, Node) #Prune
		self.operator = aOperator
		self.operand = aOperand

class ExpressionStatement(object):
	__slots__ = [
		"expression", # Expression
		"line" # int
	]

	def __init__(self, aExpression):
		assert isinstance(aExpression, Expression) #Prune
		self.expression = aExpression

class FunctionParameter(object):
	__slots__ = [
		"identifier", # Identifier
		"type", # Type
		"defaultValue" # Expression
	]

	def __init__(self, aIdentifier, aType, aDefaultValue):
		assert isinstance(aIdentifier, Identifier) #Prune
		assert isinstance(aType, Type) #Prune
		assert isinstance(aDefaultValue, Expression) #Prune
		self.identifier = aIdentifier
		self.type = aType
		self.defaultValue = aDefaultValue

class FunctionFlags(object):
	__slots__ = [
		"isBetaOnly", # bool
		"isDebugOnly", # bool
		"isGlobal", # bool
		"isNative", # bool
	]

	def __init__(self, aBetaOnly, aDebugOnly, aGlobal, aNative):
		assert isinstance(aBetaOnly, bool) #Prune
		assert isinstance(aDebugOnly, bool) #Prune
		assert isinstance(aGlobal, bool) #Prune
		assert isinstance(aNative, bool) #Prune
		self.isBetaOnly = aBetaOnly
		self.isDebugOnly = aDebugOnly
		self.isGlobal = aGlobal
		self.isNative = aNative

class FunctionSignatureStatement(object):
	__slots__ = [
		"identifier", # Identifier
		"type", # Type
		"parameters", # list of FunctionParameter
		"flags", # FunctionFlags
		"line" # int
	]

	def __init__(self, aIdentifier, aType, aParameters, aFlags, aLine):
		assert isinstance(aIdentifier, Identifier) #Prune
		assert isinstance(aType, Type) #Prune
		assert isinstance(aParameters, list) #Prune
		assert isinstance(aFlags, FunctionFlags) #Prune
		assert isinstance(aLine, int) #Prune
		self.identifier = aIdentifier
		self.type = aType
		self.parameters = aParameters
		self.flags = aFlags
		self.line = aLine

class CustomEventStatement(object):
	__slots__ = [
		"identifier", # Identifier
		"line" # int
	]

	def __init__(self, aIdentifier, aLine):
		assert isinstance(aIdentifier, Identifier) #Prune
		assert isinstance(aLine, int) #Prune
		self.identifier = aIdentifier
		self.line = aLine

class DocstringStatement(object):
	__slots__ = [
		"value", # str
		"line" # int
	]

	def __init__(self, aValue, aLine):
		assert isinstance(aValue, str) #Prune
		assert isinstance(aLine, int) #Prune
		self.value = aValue
		self.line = aLine

class AssignmentStatement(object):
	__slots__ = [
		"operator", # Token
		"leftExpression", # ExpressionNode
		"rightExpression", # ExpressionNode
		"line" # int
	]

	def __init__(self, aOperator, aLeftExpression, aRightExpression, aLine):
		assert isinstance(aOperator, Token) #Prune
		assert isinstance(aLeftExpression, ExpressionNode) #Prune
		assert isinstance(aRightExpression, ExpressionNode) #Prune
		assert isinstance(aLine, int) #Prune
		self.operator = aOperator
		self.leftExpression = aLeftExpression
		self.rightExpression = aRightExpression
		self.line = aLine

class ElseStatement(object):
	__slots__ = [
		"line" # int
	]

	def __init__(self, aLine):
		assert isinstance(aLine, int) #Prune
		self.line = aLine

class ElseIfStatement(object):
	__slots__ = [
		"expression", # ExpressionNode
		"line" # int
	]

	def __init__(self, aExpression, aLine):
		assert isinstance(aExpression, ExpressionNode) #Prune
		assert isinstance(aLine, int) #Prune
		self.expression = aExpression
		self.line = aLine

class EndEventStatement(object):
	__slots__ = [
		"line" # int
	]

	def __init__(self, aLine):
		assert isinstance(aLine, int) #Prune
		self.line = aLine

class EndFunctionStatement(object):
	__slots__ = [
		"line" # int
	]

	def __init__(self, aLine):
		assert isinstance(aLine, int) #Prune
		self.line = aLine

class EndGroupStatement(object):
	__slots__ = [
		"line" # int
	]

	def __init__(self, aLine):
		assert isinstance(aLine, int) #Prune
		self.line = aLine

class EndIfStatement(object):
	__slots__ = [
		"line" # int
	]

	def __init__(self, aLine):
		assert isinstance(aLine, int) #Prune
		self.line = aLine

class EndPropertyStatement(object):
	__slots__ = [
		"line" # int
	]

	def __init__(self, aLine):
		assert isinstance(aLine, int) #Prune
		self.line = aLine

class EndStateStatement(object):
	__slots__ = [
		"line" # int
	]

	def __init__(self, aLine):
		assert isinstance(aLine, int) #Prune
		self.line = aLine

class EndStructStatement(object):
	__slots__ = [
		"line" # int
	]

	def __init__(self, aLine):
		assert isinstance(aLine, int) #Prune
		self.line = aLine

class EndWhileStatement(object):
	__slots__ = [
		"line" # int
	]

	def __init__(self, aLine):
		assert isinstance(aLine, int) #Prune
		self.line = aLine

class EventFlags(object):
	__slots__ = [
		"isNative" # bool
	]

	def __init__(self, aNative):
		assert isinstance(aNative, bool) #Prune
		self.isNative = aNative

class EventParameter(object):
	__slots__ = [
		"identifier", # Identifier
		"type", # Type
	]

	def __init__(self, aIdentifier, aType):
		assert isinstance(aIdentifier, Identifier) #Prune
		assert isinstance(aType, Type) #Prune
		self.identifier = aIdentifier
		self.type = aType

class EventSignatureStatement(object):
	__slots__ = [
		"identifier", # Identifier
		"remote", # Identifier
		"parameters", # list of EventParameter
		"flags", # EventFlags
		"line" # int
	]

	def __init__(self, aIdentifier, aRemote, aParameters, aFlags, aLine):
		assert isinstance(aIdentifier, Identifier) #Prune
		assert isinstance(aRemote, Identifier) #Prune
		assert isinstance(aParameters, list) #Prune
		assert isinstance(aFlags, EventFlags))
		assert isinstance(aLine, int) #Prune
		self.identifier = aIdentifier
		self.remote = aRemote
		self.parameters = aParameters
		self.flags = aFlags
		self.line = aLine

class GroupFlags(object):
	__slots__ = [
		"isCollapsed", # bool
		"isCollapsedOnBase", # bool
		"isCollapsedOnRef" # bool
	]

	def __init__(self, aCollapsed, aCollapsedOnBase, aCollapsedOnRef):
		assert isinstance(aCollapsed, bool) #Prune
		assert isinstance(aCollapsedOnBase, bool) #Prune
		assert isinstance(aCollapsedOnRef, bool) #Prune
		self.isCollapsed = aCollapsed
		self.isCollapsedOnBase = aCollapsedOnBase
		self.isCollapsedOnRef = aCollapsedOnRef

class GroupSignatureStatement(object):
	__slots__ = [
		"identifier", # Identifier
		"flags", # GroupFlags
		"line" # int
	]

	def __init__(self, aIdentifier, aFlags, aLine):
		assert isinstance(aIdentifier, Identifier) #Prune
		assert isinstance(aFlags, GroupFlags) #Prune
		assert isinstance(aLine, int) #Prune
		self.identifier = aIdentifier
		self.flags = aFlags
		self.line = aLine

class IfStatement(object):
	__slots__ = [
		"expression", # ExpressionNode
		"line" # int
	]

	def __init__(self, aExpression, aLine):
		assert isinstance(aExpression, ExpressionNode) #Prune
		assert isinstance(aLine, int) #Prune
		self.expression = aExpression
		self.line = aLine

class ImportStatement(object):
	__slots__ = [
		"identifier", # Identifier
		"line" # int
	]

	def __init__(self, aIdentifier, aLine):
		assert isinstance(aIdentifier, Identifier) #Prune
		assert isinstance(aLine, int) #Prune
		self.identifier = aIdentifier
		self.line = aLine

class PropertyFlags(object):
	__slots__ = [
		"isAuto", # bool
		"isAutoReadOnly", # bool
		"isConditional", # bool
		"isConst", # bool
		"isHidden", # bool
		"isMandatory" # bool
	]

	def __init__(self, aAuto, aAutoReadOnly, aConditional, aConst, aHidden, aMandatory):
		assert isinstance(aAuto, bool) #Prune
		assert isinstance(aAutoReadOnly, bool) #Prune
		assert isinstance(aConditional, bool) #Prune
		assert isinstance(aConst, bool) #Prune
		assert isinstance(aHidden, bool) #Prune
		assert isinstance(aMandatory, bool) #Prune
		self.isAuto = aAuto
		self.isAutoReadOnly = aAutoReadOnly
		self.isConditional = aConditional
		self.isConst = aConst
		self.isHidden = aHidden
		self.isMandatory = aMandatory

class PropertySignatureStatement(object):
	__slots__ = [
		"identifier", # Identifier
		"type", # Type
		"defaultValue", # ExpressionNode
		"flags", # PropertyFlags
		"line" # int
	]

	def __init__(self, aIdentifier, aType, aDefaultValue, aFlags, aLine):
		assert isinstance(aIdentifier, Identifier) #Prune
		assert isinstance(aType, Type) #Prune
		if aDefaultValue: #Prune
			assert isinstance(aDefaultValue, ExpressionNode) #Prune
		assert isinstance(aFlags, PropertyFlags) #Prune
		assert isinstance(aLine, int) #Prune
		self.identifier = aIdentifier
		self.type = aType
		self.defaultValue = aDefaultValue
		self.flags = aFlags
		self.line = aLine

class ReturnStatement(object):
	__slots__ = [
		"expression", # ExpressionNode
		"line" # int
	]

	def __init__(self, aExpression, aLine):
		assert isinstance(aExpression, ExpressionNode) #Prune
		assert isinstance(aLine, int) #Prune
		self.expression = aExpression
		self.line = aLine

class ScriptFlags(object):
	__slots__ = [
		"isBetaOnly", # bool
		"isConditional", # bool
		"isConst", # bool
		"isDebugOnly", # bool
		"isDefault", # bool
		"isHidden", # bool
		"isNative" # bool
	]

	def __init__(self, aBetaOnly, aConditional, aConst, aDebugOnly, aDefault, aHidden, aNative):
		assert isinstance(aBetaOnly, bool) #Prune
		assert isinstance(aConditional, bool) #Prune
		assert isinstance(aConst, bool) #Prune
		assert isinstance(aDebugOnly, bool) #Prune
		assert isinstance(aDefault, bool) #Prune
		assert isinstance(aHidden, bool) #Prune
		assert isinstance(aNative, bool) #Prune
		self.isBetaOnly = aBetaOnly
		self.isConditional = aConditional
		self.isConst = aConst
		self.isDebugOnly = aDebugOnly
		self.isDefault = aDefault
		self.isHidden = aHidden
		self.isNative = aNative

class ScriptSignatureStatement(object):
	__slots__ = [
		"identifier", # Identifier
		"extends", # Identifier
		"flags", # ScriptFlags
		"line" # int
	]

	def __init__(self, aIdentifier, aExtends, aFlags, aLine):
		assert isinstance(aIdentifier, Identifier) #Prune
		assert isinstance(aExtends, Identifier) #Prune
		assert isinstance(aFlags, ScriptFlags) #Prune
		assert isinstance(aLine, int) #Prune
		self.identifier = aIdentifier
		self.extends = aExtends
		self.flags = aFlags
		self.line = aLine

class StateFlags(object):
	__slots__ = [
		"isAuto", # bool
	]

	def __init__(self, aAuto):
		assert isinstance(aAuto, bool)
		self.isAuto = aAuto

class StateSignatureStatement(object):
	__slots__ = [
		"identifier", # Identifier
		"flags", # StateFlags
		"line" # int
	]

	def __init__(self, aIdentifier, aFlags, aLine):
		assert isinstance(aIdentifier, Identifier) #Prune
		assert isinstance(aFlags, StateFlags) #Prune
		assert isinstance(aLine, int) #Prune
		self.identifier = aIdentifier
		self.flags = aFlags
		self.line = aLine

class StructSignatureStatement(object):
	__slots__ = [
		"identifier", # Identifier
		"line" # int
	]

	def __init__(self, aIdentifier, aLine):
		assert isinstance(aIdentifier, Identifier) #Prune
		assert isinstance(aLine, int) #Prune
		self.identifier = aIdentifier
		self.line = aLine

class VariableFlags(object):
	__slots__ = [
		"isConditional", # bool
		"isConst", # bool
		"isHidden" # bool
	]

	def __init__(self, aConditional, aConst, aHidden):
		assert isinstance(aConditional, bool) #Prune
		assert isinstance(aConst, bool) #Prune
		assert isinstance(aHidden, bool) #Prune
		self.isConditional = aConditional
		self.isConst = aConst
		self.isHidden = aHidden

class VariableStatement(object):
	__slots__ = [
		"identifier", # Identifier
		"type", # Type
		"value", # ExpressionNode
		"flags", # VariableFlags
		"line" # int
	]

	def __init__(self, aIdentifier, aType, aValue, aFlags, aLine):
		assert isinstance(aIdentifier, Identifier) #Prune
		assert isinstance(aType, Type) #Prune
		if aValue: #Prune
			assert isinstance(aValue, ExpressionNode) #Prune
		assert isinstance(aFlags, VariableFlags) #Prune
		assert isinstance(aLine, int) #Prune
		self.identifier = aIdentifier
		self.type = aType
		self.value = aValue
		self.flags = aFlags
		self.line = aLine

class WhileStatement(object):
	__slots__ = [
		"line" # int
	]

	def __init__(self, aLine):
		assert isinstance(aLine, int) #Prune
		self.line = aLine

#Caprica extensions
class BreakStatement(object):
	__slots__ = [
		"line" # int
	]

	def __init__(self, aLine):
		assert isinstance(aLine, int) #Prune
		self.line = aLine

class ContinueStatement(object):
	__slots__ = [
		"line" # int
	]

	def __init__(self, aLine):
		assert isinstance(aLine, int) #Prune
		self.line = aLine

class SwitchStatement(object):
	__slots__ = [
		"expression", # ExpressionNode
		"line" # int
	]

	def __init__(self, aExpression, aLine):
		assert isinstance(aExpression, ExpressionNode) #Prune
		assert isinstance(aLine, int) #Prune
		self.expression = aExpression
		self.line = aLine

class SwitchCaseStatement(object):
	__slots__ = [
		"expression", # ExpressionNode
		"line" # int
	]

	def __init__(self, aExpression, aLine):
		assert isinstance(aExpression, ExpressionNode) #Prune
		assert isinstance(aLine, int) #Prune
		self.expression = aExpression
		self.line = aLine

class SwitchDefaultStatement(object):
	__slots__ = [
		"line" # int
	]

	def __init__(self, aLine):
		assert isinstance(aLine, int) #Prune
		self.line = aLine

class EndSwitchStatement(object):
	__slots__ = [
		"line" # int
	]

	def __init__(self, aLine):
		assert isinstance(aLine, int) #Prune
		self.line = aLine

class ForCounter(object):
	__slots__ = [
		"identifier", # Identifier
		"type", # Type
		"expression" # ExpressionNode
	]

	def __init__(self, aIdentifier, aType, aExpression):
		assert isinstance(aIdentifier, Identifier) #Prune
		if aType: #Prune
			assert isinstance(aType, Type) #Prune
		assert isinstance(aExpression, ExpressionNode) #Prune
		self.identifier = aIdentifier
		self.type = aType
		self.expression = aExpression

class ForStatement(object):
	__slots__ = [
		"counter", # ForCounter 
		"toExpression", # ExpressionNode
		"stepExpression", # ExpressionNode
		"line" # int
	]

	def __init__(self, aCounter, aToExpression, aStepExpression, aLine):
		assert isinstance(aCounter, ForCounter) #Prune
		assert isinstance(aToExpression, ExpressionNode) #Prune
		if aStepExpression: #Prune
			assert isinstance(aStepExpression, ExpressionNode) #Prune
		assert isinstance(aLine, int) #Prune
		self.counter = aCounter
		self.toExpression = aToExpression
		self.stepExpression = aStepExpression
		self.line = aLine

class EndForStatement(object):
	__slots__ = [
		"line" # int
	]

	def __init__(self, aLine):
		assert isinstance(aLine, int) #Prune
		self.line = aLine

class ForEachElement(object):
	__slots__ = [
		"identifier", # Identifier
		"type", # Type
		"isAuto" # bool
	]

	def __init__(self, aIdentifier, aType, aAuto):
		assert isinstance(aIdentifier, Identifier) #Prune
		if aType: #Prune
			assert isinstance(aType, Type) #Prune
		else: #Prun
			assert isinstance(aAuto, bool) #Prun
		self.identifier = aIdentifier
		self.type = aType
		self.isAuto = aAuto

class ForEachStatement(object):
	__slots__ = [
		"element", # ForEachElement
		"expression", # ExpressionNode
		"line" # int
	]

	def __init__(self, aElement, aExpression, aLine):
		assert isinstance(aElement, ForEachElement) #Prune
		assert isinstance(aExpression, ExpressionNode) #Prune
		assert isinstance(aLine, int) #Prune
		self.element = aElement
		self.expression = aExpression
		self.line = aLine

class EndForEachStatement(object):
	__slots__ = [
		"line" # int
	]

	def __init__(self, aLine):
		assert isinstance(aLine, int) #Prune
		self.line = aLine

class DoStatement(object):
	__slots__ = [
		"line" # int
	]

	def __init__(self, aLine):
		assert isinstance(aLine, int) #Prune
		self.line = aLine

class LoopWhileStatement(object):
	__slots__ = [
		"expression", # ExpressionNode
		"line" # int
	]

	def __init__(self, aExpression, aLine):
		assert isinstance(aExpression, ExpressionNode) #Prune
		assert isinstance(aLine, int) #Prune
		self.expression = aExpression
		self.line = aLine
#End of Caprica extensions

class SyntacticError(Exception):
	def __init__(self, aMessage, aLine):
	# aMessage: string
	# aLine: int
		self.message = aMessage
		self.line = aLine

class Syntactic(object):
	__slots__ = [
		"stack", # list of various objects
		"tokenIndex", # int
		"tokenCount", # int
		"tokens", # list of Token
		"line" # int
	]

	def __init__(self):
		self.stack = None

	def Reset(self, aCaprica):
		pass

	def Abort(self, aMessage):
	# aMessage: string
		if self.tokenIndex >= self.tokenCount and self.tokenCount > 0:
			self.tokenIndex -= 1
		raise SyntacticError(aMessage, self.tokens[self.tokenIndex].line)

	def Accept(self, aToken):
	# aToken: Token
		if self.tokenIndex < self.tokenCount:
			if self.tokens[self.tokenIndex].type == aToken:
				self.tokenIndex += 1
				return True
		return False

	def Expect(self, aToken):
	# aToken: Token
		if self.tokenIndex < self.tokenCount:
			if self.tokens[self.tokenIndex].type == aToken:
				self.tokenIndex += 1
				if self.tokenIndex - 1 < self.tokenCount:
					return self.tokens[self.tokenIndex - 1]
				else:
					return None
			self.Abort("Expected a %s symbol instead of a %s symbol." % (TokenDescription[aToken], TokenDescription[self.tokens[self.tokenIndex].type]))
		self.Abort("Expected a %s symbol but no tokens remain." % (TokenDescription[aToken]))

	def Peek(self, aN = 1):
	# aN: int
		i = self.tokenIndex + aN
		if i < self.tokenCount:
			return self.tokens[i]
		return None

	def PeekBackwards(self, aN = 1):
	# aN: int
		i = self.tokenIndex - aN
		if i >= 0:
			return self.tokens[i]
		return None

	def Consume(self):
		if self.tokenIndex < self.tokenCount:
			self.tokenIndex += 1
			return
		self.Abort("No tokens remain.")

	def AcceptFlags(self, aFlags):
	# aFlags: List of TokenEnum
		if aFlags:
			successfulFlags = []
			attempts = len(aFlags)
			while attempts > 0:
				i = 0
				flagCount = len(aFlags)
				while i < flagCount:
					if self.Accept(aFlags[i]):
						successfulFlags.append(aFlags.pop(i))
						break
					i += 1
				if attempts == len(aFlags):
					if successfulFlags:
						return successfulFlags
					else:
						return None
				attempts -= 1
			return successfulFlags
		return None

	def AcceptType(self, aBaseTypes):
	# aBaseTypes: bool
		result = None
		if self.Accept(TokenEnum.IDENTIFIER):
			result = [self.PeekBackwards().value]
			while self.Accept(TokenEnum.COLON):
				result.append(self.PeekBackwards().value)
			return result
		elif aBaseTypes and (self.Accept(TokenEnum.kBOOL) or self.Accept(TokenEnum.kFLOAT) or self.Accept(TokenEnum.kINT) or self.Accept(TokenEnum.kSTRING) or self.Accept(TokenEnum.kVAR)):
			result = [self.PeekBackwards().value]
			return result
		else:
			return None

	def ExpectType(self, aBaseTypes):
	# aBaseTypes: bool
		if self.Accept(TokenEnum.IDENTIFIER):
			result = [self.PeekBackwards().value]
			while self.Accept(TokenEnum.COLON):
				self.Expect(TokenEnum.IDENTIFIER)
				result.append(self.PeekBackwards().value)
			return result
		elif aBaseTypes and (self.Accept(TokenEnum.kBOOL) or self.Accept(TokenEnum.kFLOAT) or self.Accept(TokenEnum.kINT) or self.Accept(TokenEnum.kSTRING) or self.Accept(TokenEnum.kVAR)):
			return [self.PeekBackwards().value]
		else:
			raise SyntacticError("Expected a type identifier.", self.line)

	def Property(self, aType):
	# aType: Type
		self.Expect(TokenEnum.IDENTIFIER)
		name = self.PeekBackwards()
		value = None
		flags = None
		if self.Accept(TokenEnum.ASSIGN):
			if not self.Expression():
				self.Abort("Expected an expression.")
			value = self.Pop()
			flags = self.AcceptFlags([TokenEnum.kAUTOREADONLY, TokenEnum.kAUTO, TokenEnum.kCONST, TokenEnum.kMANDATORY, TokenEnum.kHIDDEN, TokenEnum.kCONDITIONAL])
			if TokenEnum.kAUTO in flags and TokenEnum.kAUTOREADONLY in flags:
				self.Abort("A property cannot have both the AUTO and the AUTOREADONLY flag.")
			if TokenEnum.kAUTO in flags:
				pass
			elif TokenEnum.kAUTOREADONLY in flags:
				pass
			else:
				self.Abort("Properties initialized with a value require either the AUTO or the AUTOREADONLY flag.")
		else:
			flags = self.AcceptFlags([TokenEnum.kAUTOREADONLY, TokenEnum.kAUTO, TokenEnum.kCONST, TokenEnum.kMANDATORY, TokenEnum.kHIDDEN, TokenEnum.kCONDITIONAL])
		if flags:
			if TokenEnum.kAUTO not in flags:
				if TokenEnum.kCONDITIONAL in flags:
					self.Abort("Only AUTO properties can have the CONDITIONAL flag.")
				elif TokenEnum.kCONST in flags:
					self.Abort("Only AUTO properties can have the CONST flag.")
		return PropertySignature(self.line, name, aType, flags, value)

	def FunctionParameters(self):
		parameters = []
		typ = self.ExpectType(True)
		array = False
		if self.Accept(TokenEnum.LEFTBRACKET):
			self.Expect(TokenEnum.RIGHTBRACKET)
			array = True
		typ = Type(typ, array, False)
		name = self.Expect(TokenEnum.IDENTIFIER)
		value = None
		if self.Accept(TokenEnum.ASSIGN):
			value = self.ExpectExpression()
		parameters.append(ParameterSignature(self.line, name, typ, value))
		while self.Accept(TokenEnum.COMMA):
			typ = self.ExpectType(True)
			array = False
			if self.Accept(TokenEnum.LEFTBRACKET):
				self.Expect(TokenEnum.RIGHTBRACKET)
				array = True
			typ = Type(typ, array, False)
			name = self.Expect(TokenEnum.IDENTIFIER)
			value = None
			if self.Accept(TokenEnum.ASSIGN):
				value = self.ExpectExpression()
			parameters.append(ParameterSignature(self.line, name, typ, value))
		return parameters

	def EventParameters(self, aRemote):
	# aRemote: List of string
		parameters = []
		typ = self.ExpectType(True)
		array = False
		if self.Accept(TokenEnum.LEFTBRACKET):
			self.Expect(TokenEnum.RIGHTBRACKET)
			array = True
		if aRemote:
			if array:
				self.Abort("The first parameter in a remote/custom event cannot be an array.")
			if ":".join(typ) != ":".join(aRemote):
				self.Abort("The first parameter in a remote/custom event has to have the same type as the script that emits the event.")
		typ = Type(typ, array, False)
		name = self.Expect(TokenEnum.IDENTIFIER)
		parameters.append(ParameterSignature(self.line, name, typ, None))
		while self.Accept(TokenEnum.COMMA):
			typ = self.ExpectType(True)
			array = False
			if self.Accept(TokenEnum.LEFTBRACKET):
				self.Expect(TokenEnum.RIGHTBRACKET)
				array = True
			typ = Type(typ, array, False)
			name = self.Expect(TokenEnum.IDENTIFIER)
			parameters.append(ParameterSignature(self.line, name, typ, None))
		return parameters

	def Function(self, aType):
	# aType: Type
		self.Expect(TokenEnum.IDENTIFIER)
		name = self.PeekBackwards()
		parameters = None
		nextToken = self.Peek()
		self.Expect(TokenEnum.LEFTPARENTHESIS)
		if nextToken and nextToken.type != TokenEnum.RIGHTPARENTHESIS:
			parameters = self.FunctionParameters()
		self.Expect(TokenEnum.RIGHTPARENTHESIS)
		return FunctionSignature(self.line, name, aType, self.AcceptFlags([TokenEnum.kNATIVE, TokenEnum.kGLOBAL, TokenEnum.kDEBUGONLY, TokenEnum.kBETAONLY]), parameters)

	def Shift(self, aItem = None):
	# aItem: Instance of a class that inherits from Node
		if aItem:
			self.stack.append(aItem)
		else:
			self.stack.append(self.PeekBackwards())

	def Pop(self):
		if len(self.stack) > 0:
			return self.stack.pop()
		else:
			return None

	def ReduceBinaryOperator(self):
		operand2 = self.Pop()
		operator = self.Pop()
		operand1 = self.Pop()
		self.Shift(BinaryOperatorNode(operator, operand1, operand2))

	def ReduceUnaryOperator(self):
		operand = self.Pop()
		operator = self.Pop()
		self.Shift(UnaryOperatorNode(operator, operand))

	def Expression(self):
		def Reduce():
			self.Shift(ExpressionNode(self.Pop()))

		self.AndExpression()
		while self.Accept(TokenEnum.OR):
			self.Shift()
			self.AndExpression()
			self.ReduceBinaryOperator()
		Reduce()
		return True

	def AndExpression(self):
		self.BoolExpression()
		while self.Accept(TokenEnum.AND):
			self.Shift()
			self.BoolExpression()
			self.ReduceBinaryOperator()
		return True

	def BoolExpression(self):
		self.AddExpression()
		while self.Accept(TokenEnum.EQUAL) or self.Accept(TokenEnum.NOTEQUAL) or self.Accept(TokenEnum.GREATERTHANOREQUAL) or self.Accept(TokenEnum.LESSTHANOREQUAL) or self.Accept(TokenEnum.GREATERTHAN) or self.Accept(TokenEnum.LESSTHAN):
			self.Shift()
			self.AddExpression()
			self.ReduceBinaryOperator()
		return True

	def AddExpression(self):
		self.MultExpression()
		while self.Accept(TokenEnum.ADDITION) or self.Accept(TokenEnum.SUBTRACTION):
			self.Shift()
			self.MultExpression()
			self.ReduceBinaryOperator()
		return True

	def MultExpression(self):
		self.UnaryExpression()
		while self.Accept(TokenEnum.MULTIPLICATION) or self.Accept(TokenEnum.DIVISION) or self.Accept(TokenEnum.MODULUS):
			self.Shift()
			self.UnaryExpression()
			self.ReduceBinaryOperator()
		return True

	def UnaryExpression(self):
		unaryOp = False
		if self.Accept(TokenEnum.SUBTRACTION) or self.Accept(TokenEnum.NOT):
			self.Shift()
			unaryOp = True
		self.CastAtom()
		if unaryOp:
			self.ReduceUnaryOperator()
		return True

	def CastAtom(self):
		self.DotAtom()
		if self.Accept(TokenEnum.kAS) or self.Accept(TokenEnum.kIS):
			self.Shift()
			nextToken = self.Peek()
			if nextToken and nextToken.type == TokenEnum.COLON:
				self.Shift(IdentifierNode(self.ExpectType(False)))
			else:
				if self.tokens[self.tokenIndex].type == TokenEnum.IDENTIFIER or self.tokens[self.tokenIndex].type == TokenEnum.kBOOL or self.tokens[self.tokenIndex].type == TokenEnum.kFLOAT or self.tokens[self.tokenIndex].type == TokenEnum.kINT or self.tokens[self.tokenIndex].type == TokenEnum.kSTRING or self.tokens[self.tokenIndex].type == TokenEnum.kVAR:
					self.Consume()
				else:
					self.Abort("Expected a type.")
				self.Shift(IdentifierNode(self.PeekBackwards()))
			self.ReduceBinaryOperator()
		return True

	def DotAtom(self):
		if self.Accept(TokenEnum.kFALSE) or self.Accept(TokenEnum.kTRUE) or self.Accept(TokenEnum.FLOAT) or self.Accept(TokenEnum.INT) or self.Accept(TokenEnum.STRING) or self.Accept(TokenEnum.kNONE):
			self.Shift(ConstantNode(self.PeekBackwards()))
			return True
		elif self.Accept(TokenEnum.SUBTRACTION) and (self.Accept(TokenEnum.INT) or self.Expect(TokenEnum.FLOAT)):
			self.Shift(ConstantNode(UnaryOperatorNode(self.PeekBackwards(2), self.PeekBackwards(1))))
			return True
		elif self.ArrayAtom():
			while self.Accept(TokenEnum.DOT):
				self.Shift()
				self.ArrayFuncOrId()
				self.ReduceBinaryOperator()
			return True

	def ArrayAtom(self):
		def Reduce():
			temp = self.Pop()
			self.Shift(ArrayAtomNode(self.Pop(), temp))

		self.Atom()
		if self.Accept(TokenEnum.LEFTBRACKET):
			self.Expression()
			self.Expect(TokenEnum.RIGHTBRACKET)
			Reduce()
		return True

	def Atom(self):
		if self.Accept(TokenEnum.kNEW):
			typ = self.ExpectType(True)
			if self.Accept(TokenEnum.LEFTBRACKET):
				size = self.ExpectExpression()
				self.Expect(TokenEnum.RIGHTBRACKET)
				self.Shift(ArrayCreationNode(typ, size))
			else:
				self.Shift(StructCreationNode(typ))
				typ = ":".join(typ)
				typUpper = typ.upper()
				if typUpper == "BOOL" or typUpper == "FLOAT" or typUpper == "INT" or typUpper == "STRING" or typUpper == "VAR":
					raise SyntacticError("'%s' is a type, not a struct." % typ, self.line)
			return True
		elif self.Accept(TokenEnum.LEFTPARENTHESIS):
			self.Shift()
			self.Expression()
			self.Expect(TokenEnum.RIGHTPARENTHESIS)
			expr = self.Pop()
			self.Pop()
			self.Shift(expr)
			return True
		elif self.FuncOrId():
			return True

	def ArrayFuncOrId(self):
		def Reduce():
			temp = self.Pop()
			self.Shift(ArrayFuncOrIdNode(self.Pop(), temp))

		self.FuncOrId()
		if self.Accept(TokenEnum.LEFTBRACKET):
			self.Expression()
			self.Expect(TokenEnum.RIGHTBRACKET)
			Reduce()
		return True

	def FuncOrId(self):
		nextToken = self.Peek()
		if nextToken and nextToken.type == TokenEnum.LEFTPARENTHESIS:
			self.FunctionCall()
			return True
		elif self.Accept(TokenEnum.kLENGTH):
			self.Shift(LengthNode())
			return True
		elif self.Accept(TokenEnum.IDENTIFIER) or self.Accept(TokenEnum.kSELF) or self.Accept(TokenEnum.kPARENT):
			self.Shift(IdentifierNode(self.PeekBackwards()))
			return True
		else:
			self.Abort("Expected a function call, and identifier, or the LENGTH keyword")

	def FunctionCall(self):
		def Reduce():
			arguments = []
			temp = self.Pop() # Right parenthesis
			temp = self.Pop()
			while temp.type == NodeEnum.FUNCTIONCALLARGUMENT:
				arguments.insert(0, temp)
				temp = self.Pop()
			self.Shift(FunctionCallNode(self.Pop(), arguments))

		def Argument():
			ident = None
			nextToken = self.Peek()
			if nextToken and nextToken.type == TokenEnum.ASSIGN:
				self.Expect(TokenEnum.IDENTIFIER)
				ident = self.PeekBackwards()
				self.Expect(TokenEnum.ASSIGN)
			self.Expression()
			expr = self.Pop()
			self.Shift(FunctionCallArgument(ident, expr))
			return True

		self.Expect(TokenEnum.IDENTIFIER)
		self.Shift()
		self.Expect(TokenEnum.LEFTPARENTHESIS)
		self.Shift()
		if self.Accept(TokenEnum.RIGHTPARENTHESIS):
			self.Shift()
			Reduce()
			return True
		else:
			Argument()
			while self.Accept(TokenEnum.COMMA):
				Argument()
			self.Expect(TokenEnum.RIGHTPARENTHESIS)
			self.Shift()
			Reduce()
			return True

	def ExpressionOrAssignment(self):
		self.Expression()
		left = self.Pop()
		if self.Accept(TokenEnum.ASSIGN) or self.Accept(TokenEnum.ASSIGNADDITION) or self.Accept(TokenEnum.ASSIGNSUBTRACTION) or self.Accept(TokenEnum.ASSIGNMULTIPLICATION) or self.Accept(TokenEnum.ASSIGNDIVISION) or self.Accept(TokenEnum.ASSIGNMODULUS):
			operator = self.PeekBackwards()
			self.Expression()
			right = self.Pop()
			return Assignment(self.line, left, right)
		elif self.tokenIndex >= self.tokenCount or self.tokens[self.tokenIndex] == None:
			return Expression(self.line, left)

	def Variable(self, aType):
	# aType: Type
		self.Expect(TokenEnum.IDENTIFIER)
		name = self.PeekBackwards()
		value = None
		if self.Accept(TokenEnum.ASSIGN):
			self.Expression()
			value = self.Pop()
		return Variable(self.line, name, aType, self.AcceptFlags([TokenEnum.kCONDITIONAL, TokenEnum.kCONST, TokenEnum.kHIDDEN]), value)

	def ExpectExpression(self):
		if not self.Expression():
			self.Abort("Expected an expression")
		return self.Pop()

	def Process(self, aTokens):
	# aTokens: List of Token
		if not aTokens:
			return None
		
		result = None
		self.tokens = aTokens
		self.tokenIndex = 0
		self.tokenCount = len(self.tokens)
		self.line = self.tokens[self.tokenIndex].line
		self.stack = []

		tokenType = self.tokens[0].type
		if tokenType == TokenEnum.kBOOL or tokenType == TokenEnum.kFLOAT or tokenType == TokenEnum.kINT or tokenType == TokenEnum.kSTRING or tokenType == TokenEnum.kVAR:
			self.Consume()
			typ = self.PeekBackwards()
			array = False
			if self.Accept(TokenEnum.LEFTBRACKET):
				self.Expect(TokenEnum.RIGHTBRACKET)
				array = True
			typ = Type([typ.value], array, False)
			if self.Accept(TokenEnum.kPROPERTY):
				result = self.Property(typ)
			elif self.Accept(TokenEnum.kFUNCTION):
				result = self.Function(typ)
			else:
				result = self.Variable(typ)
		elif tokenType == TokenEnum.IDENTIFIER:
			typ = None
			nextToken = self.Peek()
			if nextToken:
				if nextToken.type == TokenEnum.COLON:
					typ = self.ExpectType(False)
					if typ:
						array = False
						if self.Accept(TokenEnum.LEFTBRACKET):
							self.Expect(TokenEnum.RIGHTBRACKET)
							array = True
						typ = Type(typ, array, False)
						if self.Accept(TokenEnum.kPROPERTY):
							result = self.Property(typ)
						elif self.Accept(TokenEnum.kFUNCTION):
							result = self.Function(typ)
						else:
							result = self.Variable(typ)
				elif nextToken.type == TokenEnum.LEFTBRACKET:
					nextToken = self.Peek(2)
					if nextToken:
						if nextToken.type == TokenEnum.RIGHTBRACKET:
							typ = Type([self.Expect(TokenEnum.IDENTIFIER).value], True, False)
							self.Consume()
							nextToken = self.Peek()
							self.Consume()
							if nextToken:
								if nextToken.type == TokenEnum.kFUNCTION:
									self.Consume()
									result = self.Function(typ)
								elif nextToken.type == TokenEnum.kPROPERTY:
									self.Consume()
									result = self.Property(typ)
								elif nextToken.type == TokenEnum.IDENTIFIER:
									result = self.Variable(typ)
						else:
							result = self.ExpressionOrAssignment()
				elif nextToken.type == TokenEnum.kPROPERTY:
					typ = Type([self.Expect(TokenEnum.IDENTIFIER).value], False, False)
					self.Consume()
					result = self.Property(typ)
				elif nextToken.type == TokenEnum.kFUNCTION:
					typ = Type([self.Expect(TokenEnum.IDENTIFIER).value], False, False)
					self.Consume()
					result = self.Function(typ)
				elif nextToken.type == TokenEnum.IDENTIFIER:
					result = self.Variable(Type([self.Expect(TokenEnum.IDENTIFIER).value], False, False))
				else:
					result = self.ExpressionOrAssignment()
			else:
				result = self.ExpressionOrAssignment()
		elif tokenType == TokenEnum.kIF:
			self.Consume()
			result = If(self.line, self.ExpectExpression())
		elif tokenType == TokenEnum.kELSE:
			self.Consume()
			result = Else(self.line)
		elif tokenType == TokenEnum.kELSEIF:
			self.Consume()
			result = ElseIf(self.line, self.ExpectExpression())
		elif tokenType == TokenEnum.kENDIF:
			self.Consume()
			result = EndIf(self.line)
		elif tokenType == TokenEnum.kWHILE:
			self.Consume()
			result = While(self.line, self.ExpectExpression())
		elif tokenType == TokenEnum.kENDWHILE:
			self.Consume()
			result = EndWhile(self.line)
		elif tokenType == TokenEnum.kRETURN:
			self.Consume()
			if self.tokenIndex < self.tokenCount:
				result = Return(self.line, self.ExpectExpression())
			else:
				result = Return(self.line, None)
		elif tokenType == TokenEnum.kFUNCTION:
			self.Consume()
			result = self.Function(None)
		elif tokenType == TokenEnum.kENDFUNCTION:
			self.Consume()
			result = EndFunction(self.line)
		elif tokenType == TokenEnum.kEVENT:
			self.Consume()
			nextToken = self.Peek()
			remote = None
			if nextToken and (nextToken.type == TokenEnum.DOT or nextToken.type == TokenEnum.COLON):
				remote = self.ExpectType(False)
				self.Expect(TokenEnum.DOT)
			name = self.Expect(TokenEnum.IDENTIFIER)
			nextToken = self.Peek()
			self.Expect(TokenEnum.LEFTPARENTHESIS)
			parameters = None
			if nextToken and nextToken.type != TokenEnum.RIGHTPARENTHESIS:
				parameters = self.EventParameters(remote)
			if remote and not parameters:
				self.Abort("Remote events and CustomEvents have to have a parameter defining the script that emits the event.")
			self.Expect(TokenEnum.RIGHTPARENTHESIS)
			result = EventSignature(self.line, remote, name, self.AcceptFlags([TokenEnum.kNATIVE]), parameters)
		elif tokenType == TokenEnum.kENDEVENT:
			self.Consume()
			result = EndEvent(self.line)
		elif tokenType == TokenEnum.kENDPROPERTY:
			self.Consume()
			result = EndProperty(self.line)
		elif tokenType == TokenEnum.kCUSTOMEVENT:
			self.Consume()
			result = CustomEvent(self.line, self.Expect(TokenEnum.IDENTIFIER))
		elif tokenType == TokenEnum.kGROUP:
			self.Consume()
			name = self.Expect(TokenEnum.IDENTIFIER)
			result = GroupSignature(self.line, name, self.AcceptFlags([TokenEnum.kCOLLAPSED, TokenEnum.kCOLLAPSEDONBASE, TokenEnum.kCOLLAPSEDONREF]))
		elif tokenType == TokenEnum.kENDGROUP:
			self.Consume()
			result = EndGroup(self.line)
		elif tokenType == TokenEnum.kSTRUCT:
			self.Consume()
			result = StructSignature(self.line, self.Expect(TokenEnum.IDENTIFIER))
		elif tokenType == TokenEnum.kENDSTRUCT:
			self.Consume()
			result = EndStruct(self.line)
		elif tokenType == TokenEnum.kSTATE:
			self.Consume()
			result = StateSignature(self.line, self.Expect(TokenEnum.IDENTIFIER), False)
		elif tokenType == TokenEnum.kAUTO:
			self.Consume()
			self.Expect(TokenEnum.kSTATE)
			result = StateSignature(self.line, self.Expect(TokenEnum.IDENTIFIER), True)
		elif tokenType == TokenEnum.kENDSTATE:
			self.Consume()
			result = EndState(self.line)
		elif tokenType == TokenEnum.kIMPORT:
			self.Consume()
			result = Import(self.line, self.ExpectType(False))
		elif tokenType == TokenEnum.kSCRIPTNAME:
			self.Consume()
			name = self.ExpectType(False)
			parent = None
			if self.Accept(TokenEnum.kEXTENDS):
				parent = self.ExpectType(False)
			flags = self.AcceptFlags([TokenEnum.kHIDDEN, TokenEnum.kCONDITIONAL, TokenEnum.kNATIVE, TokenEnum.kCONST, TokenEnum.kDEBUGONLY, TokenEnum.kBETAONLY, TokenEnum.kDEFAULT])
			result = ScriptSignature(self.line, name, parent, flags)
		elif tokenType == TokenEnum.DOCSTRING:
			self.Consume()
			result = Docstring(self.line, self.PeekBackwards())
		else:
			result = self.ExpressionOrAssignment()
		if self.tokenIndex < self.tokenCount:
			if self.tokens[self.tokenIndex].type == TokenEnum.KEYWORD:
				self.Abort("Unexpected %s symbol (%s)." % (TokenDescription[self.tokens[self.tokenIndex].type], KeywordDescription[self.tokens[self.tokenIndex].value]))
			else:
				self.Abort("Unexpected %s symbol (%s)." % (TokenDescription[self.tokens[self.tokenIndex].type], self.tokens[self.tokenIndex].value))
		if not result:
			self.Abort("Could not form a valid statement.")
		return result
