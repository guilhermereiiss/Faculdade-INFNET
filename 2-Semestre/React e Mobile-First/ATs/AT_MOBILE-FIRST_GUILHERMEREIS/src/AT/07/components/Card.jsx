import styled from 'styled-components';
import { BsFillTelephoneFill } from "react-icons/bs";
import { FaEnvelope } from "react-icons/fa";
import { IoLocationSharp } from "react-icons/io5";



const Geral = styled.body`
  background-color: #333;
  padding: 20px;
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
`;

const CardContainer = styled.div`
  width: 100%;
  max-width: 400px;
  margin: auto;
  background-color: #fff;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  overflow: hidden;
  display: flex;
  flex-direction: column; 
`;

const FotoContainer = styled.div`
  width: 100%;
  height: 150px;
  background-color: blue;
`;

const InformacaoContainer = styled.div`
  padding: 16px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
`;

const Nome = styled.h2`
  margin: 0;
  font-size: 1.5em;
`;

const Detalhes = styled.p`
  margin: 4px 0;
`;

const Icons = styled.div`
  display: flex;
  justify-content: space-around;
  margin-top: 16px;

`;

const Icone = styled.button`
  background-color: #eee;
  border: none;
  padding: 10px;
  border-radius: 50%;
  cursor: pointer;
  &:hover {
    background-color: #ddd;
  }
`;

const TabelaTarefas = styled.table`
  width: 100%;
  border-collapse: collapse;
  margin-top: 16px;
`;

const Th = styled.th`
  border-bottom: 2px solid #ccc;
  padding: 8px;
  text-align: left;
`;

const Td = styled.td`
  border-bottom: 1px solid #ccc;
  padding: 8px;
`;

const Checkbox = styled.input`
  margin-right: 8px;
`;

const CardFuncionario = () => {
  return (
    <Geral>
      <CardContainer>
        <FotoContainer />
        <InformacaoContainer>
          <Nome>Nome Completo</Nome>
          <Detalhes>Data de Nascimento</Detalhes>
          <Detalhes>Setor</Detalhes>
          <Detalhes>Cargo</Detalhes>

          <Icons>
            <Icone><BsFillTelephoneFill /></Icone>
            <Icone><FaEnvelope /> </Icone>
            <Icone><IoLocationSharp />
            </Icone>
          </Icons>

          <TabelaTarefas>
            <thead>
              <tr>
                <Th>Estado</Th>
                <Th>Tarefas</Th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <Td><Checkbox type="checkbox" checked /></Td>
                <Td>Tarefa 1</Td>
              </tr>
              <tr>
                <Td><Checkbox type="checkbox" /></Td>
                <Td>Tarefa 2</Td>
              </tr>
              <tr>
                <Td><Checkbox type="checkbox" /></Td>
                <Td>Tarefa 3</Td>
              </tr>
            </tbody>
          </TabelaTarefas>
        </InformacaoContainer>
      </CardContainer>
    </Geral>
  );
};

export default CardFuncionario;
