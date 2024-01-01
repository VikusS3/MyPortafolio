
/** @jsxImportSource @emotion/react */import { Fragment } from "react"
import { Fragment_fd0e7cb8f9fb4669a6805377d925fba0 } from "/utils/stateful_components"
import { Box, Button, Center, Flex, HStack, Image as ChakraImage, Link, Spacer, Text, VStack } from "@chakra-ui/react"
import Script from "next/script"
import "focus-visible/dist/focus-visible"
import NextLink from "next/link"
import NextHead from "next/head"



export default function Component() {

  return (
    <Fragment>
  <Fragment_fd0e7cb8f9fb4669a6805377d925fba0/>
  <Box>
  <Script strategy={`afterInteractive`}>
  {`document.documentElement.lang='es'`}
</Script>
  <Script src={`/js/snow.js`} strategy={`afterInteractive`}/>
  <VStack sx={{"position": "sticky", "bg": "#132d46", "borderBottom": "0.25em solid #01c38e", "paddingX": "2em", "paddingY": "1em", "zIndex": 999, "top": 0, "width": "100%"}}>
  <HStack sx={{"width": "100%"}}>
  <ChakraImage alt={`Imagen con las letras VD`} src={`logo.png`} sx={{"width": "2em", "height": "2em"}}/>
  <Text>
  {`VikusDEV`}
</Text>
  <Spacer/>
  <Box sx={{"display": ["none", "block", "block", "block"]}}>
  <Link as={NextLink} className={`nes-icon linkedin is-medium`} href={`https://www.linkedin.com/in/felix-saul-orellana-contreras-971b042a6/`} isExternal={true} sx={{"textDecoration": "none", "_hover": {"color": "#b5b0b0", "textDecoration": "none"}}}>
  {``}
</Link>
</Box>
  <Link as={NextLink} className={`nes-icon github is-medium`} href={`https://github.com/VikusS3`} isExternal={true} sx={{"textDecoration": "none", "_hover": {"color": "#b5b0b0", "textDecoration": "none"}}}>
  {``}
</Link>
  <Link as={NextLink} className={`nes-icon twitter is-medium`} href={`https://twitter.com/Vikus3S`} isExternal={true} sx={{"textDecoration": "none", "_hover": {"color": "#b5b0b0", "textDecoration": "none"}}}>
  {``}
</Link>
</HStack>
</VStack>
  <Center>
  <VStack spacing={`2em`} sx={{"widht": "100%"}}>
  <VStack sx={{"alignItems": "start", "paddingX": "2em", "width": "100%", "maxWidth": "1000px", "paddingTop": "4em"}}>
  <Flex direction={["column", "column", "column", "row", "row"]}>
  <ChakraImage alt={`Letra V de color blanco sin fondo`} src={`inicio.png`} sx={{"width": "16em", "height": "30em", "marginRight": "2em"}}/>
  <VStack alignItems={`start`}>
  <Box className={`nes-balloon from-left is-dark`}>
  <Text>
  {`Programador Full-Stack`}
</Text>
  <Text>
  {`Apasionado por la tecnología`}
</Text>
</Box>
  <Text as={`span`} sx={{"fontSize": "0.8em"}}>
  {`Hola soy Vikus y soy un programador Full-Stack, me gusta mucho la tecnología`}
  <Text as={`span`} sx={{"color": "#01c38e", "fontSize": "1em"}}>
  {` me destaco por ser autodidacta`}
</Text>
  {`!`}
</Text>
  <Text as={`span`} sx={{"fontSize": "0.8em"}}>
  {`Experto en python, php, C#, .NET, html, css, javascript, Database, entre otros`}
</Text>
  <Text as={`span`} sx={{"fontSize": "0.8em"}}>
  {`En mi encontraras un programador que se adapta a cualquier situación y que siempre busca la mejor solución`}
</Text>
  <Link as={NextLink} href={`mailto:felix21soc@gmail.com`} isExternal={true} sx={{"textDecoration": "none", "_hover": {"color": "#b5b0b0", "textDecoration": "none"}}}>
  <Button className={`nes-btn is-success`} sx={{"marginBottom": "1em", "height": "2.75em", "color": "#212529 !important", "_hover": {"color": "#FFFFFF !important"}}}>
  {`Contactame`}
</Button>
</Link>
</VStack>
</Flex>
</VStack>
</VStack>
</Center>
</Box>
  <NextHead>
  <title>
  {`VikusDEV - Programador Full Stack`}
</title>
  <meta content={`VikusDEV es un programador freelance que se dedica al desarrollo web, diseño web, desarrollo de aplicaciones, desarrollo de software, desarrollo de apl`} name={`description`}/>
  <meta content={`favicon.ico`} property={`og:image`}/>
</NextHead>
</Fragment>
  )
}
